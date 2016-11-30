import cv2
import numpy as np
import math
import scipy.io

class  Drawer(object):
	"""docstring for  """

	def __init__(self, screen, screen_heigth, screen_width, color_dict):
		self.screen = screen
		self.heigth = screen_heigth
		self.width = screen_width

		self.color_dict = color_dict

		self.tank_hight = 88
		self.tank_width = 88

		self.show_id = False
		# add your fish form into the fishForm dictionary
		self.fishForm_dict = {'thin':0, 'fat':1}
		self.fishForm = 'thin'

		self.tracker_version_dict = {'old': 0, 'latest': 1}
		self.tracker_version = 'old'

	def set_tracker_version(self, version):
		self.tracker_version = version

	def set_draw_form(self, form):
		self.fishForm = form

	def showId(self, value):
		self.show_id = value

    # add your fish form in here
	def __draw_fish(self, id, px, py, oriPx, oriPy, fishForm, color):
		if self.tracker_version_dict[self.tracker_version] == 0:
			py = self.heigth - py
			oriPy = self.heigth - oriPy


		if self.show_id:
			cv2.putText(self.screen, str(id), (px, py), cv2.FONT_HERSHEY_SIMPLEX, 0.4, (0, 0, 0))

		if self.fishForm_dict[self.fishForm] == 0:
			cv2.circle(self.screen, (px, py), 1, color)
			cv2.line(self.screen, (px, py), (oriPx, oriPy), color)
		elif self.fishForm_dict[fishForm] == 1:
			diff_x = (oriPx - px)/2
			diff_y = (oriPy - py)/2
			p_front_x = int(px + diff_x)
			p_front_y = int(py + diff_y)
			p_rear_x = int(px - diff_x)
			p_rear_y = int(py - diff_y)
			cv2.line(self.screen, (px, py), (p_front_x, p_front_y), color, 2)
			cv2.line(self.screen, (px, py), (p_rear_x, p_rear_y), color)
		else:
			cv2.circle(self.screen, (px, py), 1, color)
			cv2.line(self.screen, (px, py), (oriPx, oriPy), color)

	def draw(self, dat):
		self.screen[:,:] = (255,255,255)
		for k,v in dat.iteritems():
			(px, py) = self.__cm2pixel( (dat[k])[0], (dat[k])[1])
			angle = (dat[k])[2]
			(oriPx, oriPy) = self.__getOriPoint(px, py, angle)
			color = self.color_dict[k]
			self.__draw_fish(k, px, py, oriPx, oriPy, self.fishForm, color)
		return self.screen


	def __getOriPoint(self, x, y, angle):
		if self.tracker_version_dict[self.tracker_version] == 1:
			angle = -angle;

		s = math.sin(angle)
		c = math.cos(angle)

		x_shift = x + 10 * c
		y_shift = y + 10 * s

		return (int(x_shift),int(y_shift))

	def __cm2pixel(self,x,y):
		px = self.width * x / self.tank_width
		py = self.heigth * y / self.tank_hight
		return (int(px),int(py))


	def setTank(self,tank_width,tank_hight):
		""" unit cm """
		self.tank_hight = tank_hight
		self.tank_width = tank_width