from manim import *
import numpy as np

class GradientDescent(Scene):
    def construct(self):

        # Title for the gradient descent visualization
        title = Tex("Gradient Descent").scale(1.5)
        self.play(Write(title))
        self.play(title.animate.shift(UP * 3))


        #intro scene
        intro = Tex("Gradient Descent finds optimal weights by minimizing the cost function.",font_size=36,color=BLUE).scale(1.1)

        # Display the text
        self.play(Write(intro))
        self.wait(2)

        # Remove the text
        self.play(FadeOut(intro))

        # Create a coordinate system for the data points
        axes = Axes(
            x_range=[0, 6],
            y_range=[0, 6],
            x_length=6,
            y_length=6,
            axis_config={ "numbers_to_include": np.arange(0, 6, 1)
            }
        )
        axes.scale(0.6).shift(LEFT * 3)
        x_label = axes.get_x_axis_label("x").set_color(BLUE)
        y_label = axes.get_y_axis_label("y").set_color(BLUE)
        grid_labels = VGroup(x_label, y_label)

        # Display the coordinate system for the left plot
        self.play(Create(axes), Write(grid_labels))

        # Generate random data points
        points = np.array([[np.random.uniform(1, 5), np.random.uniform(1, 5)] for _ in range(40)])
        dots = VGroup(*[Dot(axes.c2p(x, y)) for x, y in points])
        self.play(Create(dots))

        # Initialize values for w and b
        w, b = np.random.uniform(0.5, 1.5), np.random.uniform(0.5, 1.5)

        # Store w, b values along the way
        path_points = [(w, b)]

        # Gradient descent algorithm (calculate w, b updates and store them)
        learning_rate = 0.01
        for _ in range(20):
            # Calculate gradients
            dw = -2 * np.mean(points[:, 0] * (points[:, 1] - (w * points[:, 0] + b)))
            db = -2 * np.mean(points[:, 1] - (w * points[:, 0] + b))

            # Update w and b
            w_new, b_new = w - learning_rate * dw, b - learning_rate * db

            # Store the updated w, b values
            path_points.append((w_new, b_new))

            # Update w and b
            w, b = w_new, b_new

            # Stop if gradients are small
            if np.linalg.norm([dw, db]) < 0.01:
                break

        # Create a coordinate system for the contour plot (right plot)
        contour_axes = Axes(
            x_range=[w - 0.5, w + 0.5],  # Adjust x-range based on final w
            y_range=[b - 0.5, b + 0.5],  # Adjust y-range based on final b
            x_length=6,
            y_length=6,
        )

        contour_axes.scale(0.6).shift(RIGHT * 3)

        contour_x_label = contour_axes.get_x_axis_label("w").set_color(RED)
        contour_y_label = contour_axes.get_y_axis_label("b").set_color(RED)
        contour_grid_labels = VGroup(contour_x_label, contour_y_label)

        # Display the coordinate system for the contour plot
        self.play(Create(contour_axes), Write(contour_grid_labels))

        # Create the contour plot centered around the final w, b values
        def get_contour_ellipses(w, b):
            levels = [0.1, 0.2, 0.5, 1, 1.5]
            ellipses = VGroup()
            for level in levels:
                ellipse = Ellipse(
                    width=level * 2,
                    height=level,
                    stroke_width=2,
                    color=RED,
                ).move_to(contour_axes.c2p(w, b))  # Move to the final w, b
                ellipses.add(ellipse)
            return ellipses

        # Create the contour plot
        contour = get_contour_ellipses(w, b)
        contour.rotate(30 * DEGREES)

        self.play(Create(contour))

        # Best fit line animation based on the gradient descent updates
        def get_best_fit_line(w, b):
            return axes.plot(lambda x: w * x + b, color=WHITE)

        # Create the initial best fit line
        best_fit_line = get_best_fit_line(path_points[0][0], path_points[0][1])
        self.play(Create(best_fit_line))

        # Display final w, b values
        wb_text = MathTex(f"w = {w:.2f}, \\ b = {b:.2f}")
        wb_text.to_corner(DOWN + ORIGIN)

        # Update best fit line and point along the path
        for (w_, b_) in path_points:
            updated_best_fit_line = get_best_fit_line(w_, b_)
            updated_point_on_contour = Dot(contour_axes.c2p(w_, b_), color=YELLOW)
            updated_wb_text = MathTex(f"w = {w_:.2f}, \\ b = {b_:.2f}").to_corner(DOWN + ORIGIN)
            self.play(
                Transform(best_fit_line, updated_best_fit_line),
                Transform(updated_point_on_contour, updated_point_on_contour),
                Transform(wb_text, updated_wb_text),
                run_time=0.5
            )
        self.wait(2)


