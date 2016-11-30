class  DataHandler(object):
    def __init__(self, dat):
        self.dat = dat
        self.begin_ID = int(dat[0][0])
        self.end_ID = int(dat[dat.shape[0]-1][0])
        self.fish_Num = dat.shape[1] // 5

    def get_fish_num(self):
        return self.fish_Num

    def get_begin_ID(self):
        return self.begin_ID

    def get_end_ID(self):
        return self.end_ID

    def get_frame_dat(self, frame_id):
        if(frame_id < self.begin_ID or frame_id > self.end_ID ):
            print 'frame_id error in tracking data handler'
            return None
        else:
            row = self.dat[frame_id - self.begin_ID][1:]
            fish_dict = {}
            for i in range(self.fish_Num):
                begin = 5*(i-1)
                # fish ids
                id = int(row[begin])
                # x coordinate
                x = row[begin+1]
                # y corrdinate
                y = row[begin+2]
                # deg = row[begin+3]
                # orientation in radians
                rad = row[begin+4]
                fish_dict[id] = [x,y,rad]
        return fish_dict
