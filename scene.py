from math import *
from manim import *

#manim -pqk scene.py 
#manim -pqk --format=png scene.py 

# Colors
WHITE = '#FFFFFF'
BLACK = '#000000'
RED = '#C02020'
GREEN = '#70FF70'
BLUE = '#8080FF'
PURE_RED = '#FF0000'
PURE_GREEN = '#00FF00'
PURE_BLUE = '#0000FF'

class Part2Q1(ThreeDScene):
    def Lerp(self , starting_point , ending_point , t , flag=0):
        return [int(a*(1-t)+b*t) for a, b in zip(starting_point, ending_point)] if flag else [a*(1-t)+b*t for a, b in zip(starting_point, ending_point)]
    def construct(self):
        self.camera.background_color = '#101020'
        self.camera.background_color = '#101020'
        #self.camera.light_source.move_to(OUT*20)
        self.set_camera_orientation(phi=2*PI/5, theta=PI/4)
        self.set_camera_orientation(zoom=1.5)
        axes = ThreeDAxes(
            x_range=(-3, 3, 1), y_range=(-3, 3, 1), z_range=(-2, 2, 1),
            x_length=6, y_length=6, z_length=4
        ).set_opacity(0.25)
        x_axis_label_rotation_angle , x_axis_label_rotation_axis = angle_axis_from_quaternion(quaternion_mult(quaternion_from_angle_axis(angle=PI, axis=OUT, axis_normalized=True) , quaternion_from_angle_axis(angle=PI/2, axis=RIGHT, axis_normalized=True)))
        y_axis_label_rotation_angle , y_axis_label_rotation_axis = angle_axis_from_quaternion(quaternion_mult(quaternion_from_angle_axis(angle=PI/2, axis=OUT, axis_normalized=True) , quaternion_from_angle_axis(angle=PI/2, axis=RIGHT, axis_normalized=True)))
        x_axis_label = axes.get_x_axis_label(MathTex("x" , color = RED).scale(1) , edge=RIGHT , buff=1).move_to([3.25,0,0]).rotate(x_axis_label_rotation_angle , axis=x_axis_label_rotation_axis)
        y_axis_label = axes.get_y_axis_label(MathTex("y" , color = GREEN).scale(1) , edge=UP , buff=1 , rotation=0).move_to([0,3.25,0]).rotate(y_axis_label_rotation_angle , axis=y_axis_label_rotation_axis)
        z_axis_label = axes.get_z_axis_label(MathTex("z" , color = BLUE).scale(1) , edge=OUT , buff=1 , rotation=PI/2).move_to([0,0,2.25]).rotate(PI*3/4 , axis=OUT)
        axes_labels = Group(x_axis_label , y_axis_label , z_axis_label)

        self.add(axes, axes_labels)
        tumor = Sphere().set_color(WHITE).set_opacity(0.1).set_stroke_opacity(0.1)
        self.add(tumor)

        t_label = Variable(var=43.00, label=MathTex(r"\text{temperature T}"), num_decimal_places=1).scale(0.5)
        t_label.label.set_color(GREEN).rotate(PI/2, axis=RIGHT).rotate(PI*3/4, axis=OUT).move_to([-1.45,1.45,2])
        t_label.value.move_to([0,0,20])
        self.add(t_label)

        t_val = always_redraw(lambda : MathTex(f"{t_label.value.get_value():.2f}"+r"^{\circ}C").set_color(
            rgb_to_color(tuple(self.Lerp([255,140,0], [44,187,206], (t_label.value.get_value()-43)/-6, 1)))
        ).scale(0.5).rotate(PI/2, axis=RIGHT).rotate(PI*3/4, axis=OUT).move_to([-2.5,2.5,2]))
        self.add(t_val)

        partial_tumor = always_redraw(lambda : Sphere(radius=(t_label.value.get_value()-43)/-6).set_color(rgb_to_color(tuple(self.Lerp( [255,140,0] , [44*0.8,187*0.8,206*0.8] , (t_label.value.get_value()-43)/-6 , 1 )))))
        self.add(partial_tumor)
        self.wait(1)
        self.play(t_label.tracker.animate.set_value(42), run_time=1)
        self.wait(1)
        self.play(t_label.tracker.animate.set_value(41), run_time=1)
        self.wait(1)
        self.play(t_label.tracker.animate.set_value(40), run_time=1)
        self.wait(1)
        self.play(t_label.tracker.animate.set_value(39), run_time=1)
        self.wait(1)
        self.play(t_label.tracker.animate.set_value(38), run_time=1)
        self.wait(1)
        self.play(t_label.tracker.animate.set_value(37), run_time=1)
        self.wait(1)