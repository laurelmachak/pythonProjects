import arcade

arcade.open_window("Example", 600, 600)
arcade.set_background_color(arcade.color.WHITE)
arcade.start_render()

for x in range(0,601,120):
	arcade.draw_line(x,0,x,600,arcade.color.BLACK,2)

for y in range(0,601,200):
	arcade.draw_line(0,y,800,y,arcade.color.BLACK,2)

arcade.draw_text("draw_point", 3, 405, arcade.color.BLACK,2)
arcade.draw_point(60, 495, arcade.color.RED, 10)

arcade.finish_render()
arcade.run()
