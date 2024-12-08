from manim import *

import numpy as np

class LossFuncGradDesc(Scene):
    def construct(self):

        # Loss function intro
        loss_func_intro = MathTex(r"\text{Cost Function}").scale(1.5)
        loss_func_intro.color = YELLOW

        #representation of loss function components step by step
        self.play(Write(loss_func_intro))
        self.wait(2)

        #move loss function intro to the top
        self.play(loss_func_intro.animate.shift(UP*3))

        #engagment hook for the loss function 
        loss_fuc_intro_engagment = Text("Cost function is a function that measures how well the model is performing").scale(0.5).next_to(loss_func_intro, DOWN)

        self.play(Write(loss_fuc_intro_engagment.shift(DOWN*0.5)))


        # Step 1: Introduce the error term (prediction - target)
        error_term = MathTex(r"f(x^{(i)}) - y^{(i)}", color=RED).scale(1.5)
        error_explanation = Text("This is the error: the difference between predicted value and actual value.", font_size=24).next_to(error_term, DOWN)

        self.play(Write(error_term))
        self.play(Write(error_explanation))
        self.wait(3)

        # Step 2: Square the error (explanation of squaring)
        squared_error = MathTex(r"(f(x^{(i)}) - y^{(i)})^2", color=BLUE).scale(1.5)
        squared_error_explanation = Text("We square the error to avoid negative values and penalize large errors.", font_size=24).next_to(squared_error, DOWN)
        
        self.play(Transform(error_term, squared_error),Transform(error_explanation, squared_error_explanation))
        self.wait(3)

        # Step 3: Show summation over the training set and the scaling factor
        summation_term = MathTex(r"\frac{1}{m} \sum_{i=1}^{m} (f(x^{(i)}) - y^{(i)})^2", color=GREEN).scale(1.5)
        summation_explanation = Text("We sum over all training points and take the mean, scaling by 1/m.", font_size=24).next_to(summation_term, DOWN)
        
        self.play(Transform(error_term, summation_term),Transform(error_explanation, summation_explanation))
        self.wait(3)

        # Step 4: Introduce the factor of 1/2 to prepare for gradient descent
        full_loss_function = MathTex(r"J(w) = \frac{1}{2m} \sum_{i=1}^{m} (f(x^{(i)}) - y^{(i)})^2", color=YELLOW).scale(1.5)
        full_loss_function_explanation = Text("The 1/2 factor is used in gradient descent to simplify the derivative.", font_size=24).next_to(full_loss_function, DOWN)
        
        self.play(Transform(error_term, full_loss_function),Transform(error_explanation, full_loss_function_explanation))
        self.wait(3)

        # fade out the last screen
        self.play(FadeOut(full_loss_function), 
                  FadeOut(full_loss_function_explanation), 
                  FadeOut(error_term), 
                  FadeOut(error_explanation),
                  FadeOut(loss_fuc_intro_engagment),
                  FadeOut(loss_func_intro))

         # Main Title
        main_title = Text("Visualizing the Cost Function and Line Fit Relationship", font_size=32,color=YELLOW)
        main_title.to_edge(UP)
        self.play(Write(main_title))

        # Axes configurations
        axes_config = {
            "x_range": [0, 4, 1],
            "y_range": [0, 4, 1],
            "x_length": 4,
            "y_length": 4,
            "axis_config": {"include_numbers": True, "font_size": 20},
        }

        # Titles for individual graphs
        line_title = Text("Line Graph (Best Fit)", font_size=24)
        cost_title = Text("Cost Function (Error)", font_size=24)

        # Create coordinate systems
        line_axes = Axes(**axes_config).to_edge(LEFT, buff=2)
        cost_axes = Axes(**axes_config).to_edge(RIGHT, buff=2)

        line_title.next_to(line_axes, UP)
        cost_title.next_to(cost_axes, UP)

        # Add coordinate systems and titles
        self.play(Create(line_axes), Create(cost_axes))
        self.play(Write(line_title), Write(cost_title))

        # Data points on line graph
        data_points = [
            Dot(line_axes.c2p(1, 1), color=RED),
            Dot(line_axes.c2p(2, 2), color=RED),
            Dot(line_axes.c2p(3, 3), color=RED),
        ]

        for dot in data_points:
            self.play(Create(dot))

        
        # Parabola for cost function
        parabola = cost_axes.plot(lambda x: 0.5 * (x - 1) ** 2, x_range=[0, 3], color=BLUE)
        self.play(Create(parabola))

        # Step 1: Initial wrong point on cost function graph and its effect
        wrong_ws = [0.6, 1.3]
        wrong_lines = [
            line_axes.plot(lambda x, w=w: w * x, x_range=[0, 3], color=GREEN)
            for w in wrong_ws
        ]
        wrong_cost_points = [cost_axes.c2p(w, 0.5 * (w - 1) ** 2) for w in wrong_ws]

        for w, cost_point, line in zip(wrong_ws, wrong_cost_points, wrong_lines):
            # Highlight the wrong point on the cost function
            self.play(Create(Dot(cost_point, color=YELLOW)))
            # Show the line corresponding to the wrong w
            self.play(Create(line))
            self.wait(1)
            self.play(FadeOut(line))

        # Step 2: Optimal point and correct line
        optimal_w = 1
        correct_line = line_axes.plot(lambda x: optimal_w * x, x_range=[0, 3], color=YELLOW)
        optimal_cost_point = Dot(cost_axes.c2p(optimal_w, 0), color=YELLOW)

        self.play(Create(optimal_cost_point))
        self.play(Create(correct_line))
        self.wait(2)


        # Step 3: Add labels and wrap up
        optimal_label = Text("Minimal Error Achieved!", font_size=24, color=YELLOW)
        optimal_label.next_to(optimal_cost_point, DOWN*2)
        self.play(Write(optimal_label))
        self.wait(2)

        self.play(FadeOut(optimal_label))

        # Step 4: Hook for the next post about Gradient Descent
        hook_text = Text("How can we get the optimal w ?", font_size=32, color=RED)
        hook_text.move_to(DOWN * 3)  # Positioning the hook at the bottom of the screen
        hook_text.set_color(WHITE)
        self.play(Write(hook_text))
        self.wait(3)

