import numpy as np
import cv2


class Canvas:
    def __init__(self, img_size, scale=1, nc=1, pen_width = 10):
        self.img_size = img_size
        self.scale = scale
        self.nc = nc
        self.img = np.zeros((img_size, img_size, self.nc), np.uint8)
        self.shadow_img = np.ones((img_size, img_size, self.nc), np.uint8)
        self.mask = np.zeros((img_size, img_size, 1), np.uint8)
        if self.nc == 1:  # [hack]
            self.width = pen_width
        else:
            self.width = pen_width
        self.img.fill(255)
        self.mask.fill(255)
        self.shadow_img.fill(255)
        self.background_img = self.img
        self.foreground_img = self.img

    def update(self, points, color):
        num_pnts = len(points)
        c = color #0#255

        for i in range(0, num_pnts - 1):
            pnt1 = (int(points[i].x()/self.scale), int(points[i].y()/self.scale))
            pnt2 = (int(points[i + 1].x()/self.scale), int(points[i + 1].y()/self.scale))
            if self.nc == 3:
                cv2.line(self.img, pnt1, pnt2, (c, c, c), self.width)
            else:
                cv2.line(self.img, pnt1, pnt2, c, self.width)

    def update_width(self, d):
        self.width = min(20, max(1, self.width+ d.y()))
        return self.width

    def update_brushwidth(self, width):
        self.width = width
        return self.width

    def get_constraints(self):
        return self.img, self.mask

    def get_img(self):
        final_image = cv2.addWeighted(self.img, 0.25, self.shadow_img, 0.75, 0)
        return final_image #self.img

    def get_draw_img(self):
        return self.img

    def set_shadow_img(self,cv2_img):
        if cv2_img is not None:
            self.shadow_img= cv2_img

    def show_img(self):
        cv2.imshow('ImageWindow', self.img)
        cv2.waitKey()

    def get_mask(self):
        return self.mask

    def reset(self):
        self.img = np.zeros((self.img_size, self.img_size, self.nc), np.uint8)
        self.mask = np.zeros((self.img_size, self.img_size, 1), np.uint8)
        self.shadow_img = np.ones((self.img_size, self.img_size, self.nc), np.uint8)
        self.img.fill(255)
        self.mask.fill(255)
        self.shadow_img.fill(255)
