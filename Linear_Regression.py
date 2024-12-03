from manim import *
import random
import numpy as np

class LinearRegressionScene(Scene):
     def construct(self):
        # Step 1: Create Title
        title = Text("Linear Regression: Finding the Best-Fit Line", font_size=32)
        linear_regression = Text("Linear Regression", font_size=32)
        
        # Write the full title on the screen
        self.play(Write(title))
        self.wait(1)
       
        # Step 2: Split title into parts and make "Finding the Best-Fit Line" fade out
        # Create "Linear Regression" text and set position to the center
        self.play(Transform(title, linear_regression))
        self.play(title.animate.shift(UP * 3))
        self.wait(1)

        # Step 2: Set up Axes on the Right
        axes = Axes(
            x_range=[-5, 5, 1], y_range=[-5, 5, 1],
            x_length=5, y_length=5,
            axis_config={"include_numbers": True},
        ).to_edge(RIGHT)

        self.play(Create(axes))
        self.wait(1)

        # Step 3: Generate and Plot Random Points
        num_points = 10
        random_points = [
            (np.random.uniform(-4, 4), np.random.uniform(-4,4)) for _ in range(num_points)
        ]
        scatter = VGroup(*[
            Dot(point=axes.c2p(x, y), color=BLUE) for x, y in random_points
        ])
        self.play(*[FadeIn(dot, run_time=0.2) for dot in scatter])
        self.wait(1)

        # Step 4: Calculate Best-Fit Line
        x_coords = np.array([x for x, y in random_points])
        y_coords = np.array([y for x, y in random_points])
        m, b = np.polyfit(x_coords, y_coords, 1)  # Linear regression: y = mx + b

        best_fit_line = axes.plot(
            lambda x: m * x + b, color=YELLOW
        ).set_color_by_gradient(RED, YELLOW)
        self.play(Create(best_fit_line), run_time=2)

        # Step 5: Add Explanation Box with Fancy Text and Equations
        explanation_box = Rectangle(
            width=7, height=4, color=WHITE, fill_opacity=0.1
        ).to_edge(LEFT, buff=0.5)

         # Step 2: Create Explanation Text
        explanation_text = VGroup(
            Text("Linear Regression finds the line:", font_size=24),
            MathTex("y = mx + b").set_color(YELLOW),
            Text("by minimizing the Mean Squared Error (MSE):", font_size=24),
            MathTex(
                "\\text{MSE} = \\frac{1}{n} \\sum_{i=1}^n (y_i - (mx_i + b))^2"
            )
        ).arrange(DOWN, aligned_edge=ORIGIN, buff=0.5)
        explanation_text_width = explanation_text.get_width()  # Get the width of the text
        box_width = explanation_box.get_width()  # Get the width of the box
        if explanation_text_width > box_width * 0.8:  # If the text width is more than 80% of the box width
            explanation_text.scale(0.8)  # Scale the text to fit inside the box

        # Step 3: Adjust the position of the explanation text
        explanation_text.move_to(explanation_box.get_center())


        self.play(FadeIn(explanation_box))
        self.play(Write(explanation_text))
        self.wait(2)

        # Step 6: Highlight Residuals (Error Lines)
        residual_lines = VGroup(*[
            DashedLine(
                start=axes.c2p(x, y),
                end=axes.c2p(x, m * x + b),
                color=GRAY
            ) for x, y in random_points
        ])
        self.play(*[Create(line) for line in residual_lines], run_time=2)
        self.wait(2)

        # Step 7: Fade Residual Lines for Final Focus
        highlight_text = Text("Minimizing these errors!", font_size=28).next_to(
            explanation_box, DOWN, aligned_edge=LEFT, buff=1
        )
        self.play(Write(highlight_text))
        self.wait(2)

        self.play(FadeOut(residual_lines), FadeOut(highlight_text))
        self.wait(2)
