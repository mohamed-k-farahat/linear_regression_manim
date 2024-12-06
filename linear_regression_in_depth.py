from manim import *

class HousePricePrediction(Scene):
    def construct(self):
        # Introduction text
        intro_text = Text(
            "Why we use Linear Regression?",
            font_size=36,
            color=YELLOW
        ).to_edge(UP)

        # Explanation example
        example_text = Text(
            "Suppose we want to predict the price of a house given its size in sqft",
            font_size=28,
            color=WHITE
        ).next_to(intro_text, DOWN, buff=0.5)

        # Fade in the intro and example
        self.play(Write(intro_text))
        self.play(FadeIn(example_text))
        self.wait(2)


        # Define the dataset
        data = [
            ["1","1500", "300,000"],
            ["2","2000", "?"],
            ["3","2500", "500,000"],
            ["4","3000", "600,000"],
            ["5","3500", "700,000"]
        ]

        # Create the table
        table = Table(
            data,
            col_labels=[
                Text("#").scale(0.6),
                Text("House Size (sq ft)").scale(0.6),
                Text("Price ($)").scale(0.6)
            ],
            include_outer_lines=True,
        ).scale(0.7)  # Scale the table to fit the scene

        # table under the text
        table.next_to(example_text, DOWN, buff=0.5)

        # Display the table with slow stroke animation
        self.play(Create(table, lag_ratio=0.1, run_time=2))
        self.wait(2)

        # Highlight one row as an example
        example_row = table.get_rows()[2]  # 2nd row (1500, 300,000)
        self.play(Indicate(example_row, color=YELLOW))
        self.wait(2)

        # gather all mobjects in a vgroup except table
        all_mobjects = VGroup(intro_text, example_text)

        #fade the mobjects out and set the table to the left of the screen
        self.play(FadeOut(all_mobjects))
        self.play(table.animate.scale(1).to_edge(LEFT, buff=0.5))


        # Create a rectangle for the explanation header
        explanation_rect = Rectangle(
            width=14,  # Adjusted to span the screen width
            height=1.7,  # Adjusted height for the header
            color=WHITE
        ).set_fill(BLACK, opacity=0.75).to_edge(UP) 

        # write explanation text and center it on the top of the screen
        explanation = Tex("In this section, we'll focus on understanding key terminologies that form the foundation of linear regression. These terms help us describe and work with the dataset effectively.")
        explanation.color = YELLOW
        explanation.scale(0.8)

        #move text to the rectangle
        explanation.move_to(explanation_rect)
        #write the explanation
        self.play(Create(explanation_rect))
        self.play(Write(explanation))
        self.wait(2)


        #add a box for termiologies and lable it ttermiologies
        termiologies_box = Rectangle(color=WHITE, height=5, width=5).next_to(table, RIGHT, buff=0.5)
        # Terminology header inside the box
        terminology_header = Text("Terminologies", font_size=28, color=WHITE)
        #align the header to the top of the box
        terminology_header.move_to(termiologies_box.get_top()+DOWN*0.5)
        
        """termologies for machinme learning
        x = input features
        y = output predictions
        m = number of training examples
        (x, y) = one training example
        """
        # add the termology to the right of the screen and highlight the text with the termology label the same color
        terminologies = VGroup(
            Text("x = input features", font_size=24,color=BLUE),
            Text("y = output predictions", font_size=24,color=GREEN),
            Text("m = number of training examples", font_size=24,color=ORANGE),
            Text("(x, y) = one training example", font_size=24,color=PURPLE),
        ).arrange(DOWN, aligned_edge=LEFT).next_to(table, RIGHT, buff=0.5)

        termiologies_box.move_to(terminologies.get_center()) 
        
        # add termilogies in the box
        self.play(Create(termiologies_box),Write(terminology_header))

        # Animate the terms and highlight cells with background color
        for i, term in enumerate(terminologies):
            # Animate the term appearing and align it under the header
            if i == 0:
                term.next_to(terminology_header, DOWN, buff=0.5)
            else:
                term.next_to(terminologies[i-1], DOWN, buff=0.5)
            self.play(Write(term))
            self.wait(1)

            # Highlight the corresponding element in the table with background color
            if i == 0:  # "x = input features"
                cell_0 = table.get_cell((3,2))  # second row, second column
                cell_0.set_color(color=BLUE)
                self.play(Indicate(cell_0, color=BLUE))  # Indicate the cell
            elif i == 1:  # "y = output predictions"
                cell_1 = table.get_cell((3,3))  # second row, third column
                cell_1.set_color(color=GREEN)
                self.play(Indicate(cell_1, color=GREEN))  # Indicate the cell
            elif i == 2:  # "m = number of training examples"
                table.add(SurroundingRectangle(table.get_columns()[1],color=ORANGE)) 
            elif i == 3:  # "(x, y) = one training example"
                table.add(SurroundingRectangle(table.get_rows()[3],color=PURPLE)) 
            self.wait(2)
            
        # Fade out the scene and introduce a flowchart for the pipeline of linear regression
        self.play(FadeOut(VGroup(explanation, explanation_rect, termiologies_box, terminology_header, terminologies, table,cell_0,cell_1)))
        self.wait(2)

        # Title
        title = Text("Linear Regression Flowchart", font_size=36).to_edge(UP)
        self.play(Write(title))
        self.wait()

        
        # Define the rectangles for each step in the pipeline
        training_set = Rectangle(color=BLUE, height=1, width=3).to_edge(LEFT)
        training_text = Text("Training Set", font_size=24).move_to(training_set.get_center())

        learning_algo = Rectangle(color=PURPLE, height=1, width=3).next_to(training_set, RIGHT, buff=2)
        learning_text = Text("Learning Algorithm", font_size=24).move_to(learning_algo.get_center())

        cost_function = Rectangle(color=ORANGE, height=1, width=3).next_to(learning_algo, RIGHT, buff=2)
        cost_text = MathTex(r"f", font_size=45).move_to(cost_function.get_center())

        # Create the rectangles and text on the scene
        self.play(Create(training_set), Write(training_text))
        self.play(Create(learning_algo), Write(learning_text))
        self.play(Create(cost_function), Write(cost_text))

        # Create arrows connecting the rectangles
        arrow1 = Arrow(start=training_set.get_right(), end=learning_algo.get_left())
        arrow2 = Arrow(start=learning_algo.get_right(), end=cost_function.get_left())

        # Fade in the arrows 
        self.play(FadeIn(arrow1), FadeIn(arrow2))


         # Add x and y_hat labels
        x_label = Text("x", font_size=36).next_to(cost_function, UP*3, buff=0.5)
        y_hat_label = Tex(r"$\hat{y}$", font_size=42).next_to(cost_function, DOWN*3, buff=0.5)

        self.play(Write(x_label), Write(y_hat_label))

        # Create arrows for x coming from above the cost function and y_hat going out below
        arrow_in = Arrow(start=x_label.get_center(), end=cost_function.get_top())
        arrow_out = Arrow(start=cost_function.get_bottom(), end=y_hat_label.get_center())

        # Fade in the arrows for x -> cost function (from above) and cost function -> y_hat (coming out below)
        self.play(FadeIn(arrow_in), FadeIn(arrow_out))

        # Wait for a moment to observe the elements
        self.wait(5)

        #delete the rectangles and arrows from the scene
        self.play(FadeOut(VGroup(training_set, training_text, learning_algo, learning_text, cost_function, cost_text, arrow1, arrow2, x_label, y_hat_label, arrow_in, arrow_out,title)))

          # Create a smaller coordinate system
        axes = Axes(
            x_range=[0, 5],  # Adjusted to keep it compact
            y_range=[0, 10],
            axis_config={"color": BLUE},
        ).shift(LEFT * 4)  # Shift to the left so everything fits

        #scale the axex
        axes.scale(0.4)

        # Create the line f(x) = wx + b (w=2, b=1 for simplicity)
        line = axes.plot(lambda x: 2 * x + 1, color=WHITE, x_range=[0, 4.5])

        # Create multiple dummy data points (including outliers)
        points = [
            Dot(axes.c2p(1, 3), color=RED),
            Dot(axes.c2p(2, 5), color=RED),
            Dot(axes.c2p(3, 7), color=RED),
            Dot(axes.c2p(4, 9), color=RED),
            Dot(axes.c2p(1.5, 4.5), color=YELLOW),  # Outlier 1
            Dot(axes.c2p(2.5, 2), color=YELLOW),   # Outlier 2
            Dot(axes.c2p(4.5, 11), color=YELLOW)   # Outlier 3
        ]
        
        # Display the question and explanation at the top of the screen using MathTex
        question_text = MathTex(r"\text{How to represent } f?").scale(0.8).to_edge(UP)
        explanation_text = MathTex(
            r"\text{Let's start by saying for simplicity's sake that } f \text{ is a straight line.}"
        ).scale(0.7).next_to(question_text, DOWN)

        # Create a rectangle for the explanation box
        explanation_box = Rectangle(width=6, height=3, color=WHITE, fill_opacity=0.1).next_to(axes, RIGHT,buff=1)
    
        # # Create the explanation text (manually broken into lines)
        text_parts = [
            "Linear regression is a fundamental concept in machine learning.",
            "In this case, we are simplifying it to univariate linear regression,",
            "where we have a single input variable (x) and predict a single output (y).",
            "The goal is to find the best-fitting straight line through the data.",
            "This method is also called linear regression with one variable because",
            "it uses only one input variable (uni = one, variate = variable)."
        ]

        texts = VGroup(*[Tex(part, font_size=24) for part in text_parts])
        texts.arrange(DOWN, aligned_edge=ORIGIN)

        # Adjust the width of the text group to fit within the box
        texts.set_width(explanation_box.width - 0.5)

        # Position the text within the box, ensuring it starts from the top-left corner and avoids overlap
        texts.next_to(explanation_box.get_corner(UL), DR, buff=0.2)  # Adjust the buffer as needed
        texts.shift(DOWN * 0.5)

        # Create the explanation box title
        explanation_box_title = Tex("Regression with One Variable", font_size=24, color=RED_A)
        explanation_box_title.move_to(explanation_box.get_top() + DOWN * 0.3)

        #draw the line function above the explanation box
        line_function = MathTex(r"f(x) = wx + b", font_size=36,color=BLUE)
        line_function.move_to(explanation_box.get_top() + DOWN * 0)
        line_function.shift(UP*0.7)


        # Create the text and box
        self.play(Write(question_text))
        self.wait(1)
        self.play(Write(explanation_text))
        self.wait(1)

        # Create the axes and line
        self.play(Create(axes), Create(line))
        
        # Create the points and labels
        self.play(*[Create(point) for point in points])

        #type the line function above the box
        self.play(Write(line_function))

        # Create the explanation box and note text
        self.play(Create(explanation_box))
        self.play(Create(explanation_box_title))
        self.play(Write(texts), run_time=5)
        
        # Wait to end the scene
        self.wait(3)

        #fade out last scene objects
                # Fade out all elements correctly
        self.play(
            FadeOut(question_text),
            FadeOut(explanation_text),
            FadeOut(axes),
            FadeOut(line),
            *[FadeOut(point) for point in points],  # Fade out all points
            FadeOut(explanation_box),
            FadeOut(explanation_box_title),
            FadeOut(texts),
            FadeOut(line_function),
            )

        # Title for the scene
        title = Tex("How to Ensure \\( \\hat{y} \\) is the Right Answer?",color=BLUE_A)
        title.scale(1.2).to_edge(UP)

        # Explanation text
        explanation = VGroup(
            Tex("We want to ensure that our predictions \\( \\hat{y} \\) are as close as possible to"),
            Tex("the actual outputs \\( y \\). To do this, we need a way to measure how good or"),
            Tex("bad our predictions are. This is where the \\textbf{Cost Function} comes in."),
        ).arrange(DOWN, aligned_edge=LEFT).scale(0.8).next_to(title, DOWN, buff=1)

        # Introducing the Cost Function
        cost_function = MathTex("J(w, b) = \\frac{1}{2m} \\sum_{i=1}^m \\left( \\hat{y}^{(i)} - y^{(i)} \\right)^2")
        cost_function.set_color(YELLOW).scale(1).to_edge(DOWN)

        # Add the question for the next video
        next_step = Tex(
            "In the next post, we'll dive deeper into the Cost Function",
            " to understand how it works and helps us optimize \\( w \\) and \\( b \\)."
        ).scale(0.8).next_to(cost_function, UP, buff=1)

        # Animations
        self.play(Write(title))
        self.wait(1)
        self.play(FadeIn(explanation, shift=UP))
        self.wait(2)
        self.play(Write(cost_function))
        self.wait(2)
        self.play(Write(next_step))
        self.wait(5)