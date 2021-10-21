# Dennis Blaufuss
# 8458109
# 21.10.21
# Option 2 - OCR boxes


class Table:

    def __init__(self, top_left_x, top_left_y, width, height):
        # Represents a table on a page through the top left corner and width and height, relative to the top left of the page.
        # You can assume that
        # * all numbers are positive (top_left_x or top_left_y can be 0)
        # * width is larger than 0
        # * height is larger than 0
        self.top_left_x = top_left_x
        self.top_left_y = top_left_y
        self.width = width
        self.height = height

    def calculate_columns(self, ocr_boxes):
        # Returns a list of column separators relative to the top_left_x of the table without crossing OCR boxes.
        # Note that:
        # * OCR boxes are given as a list of lists (for example:  [[10, 10, 100, 5], [10, 20, 80, 5]])
        # * each box has a top_left_x, top_left_y, width and height (in that order) relative to the page (not table!)
        # * you can assume that the table itself is not crossing any OCR box;
        # * if there are no OCR boxes within the table borders return an empty list ([]).
        # * the algorithm must not create column that is totally empty (i.e has not OCR box in it);
        # * the column separator should be (approximately) in the middle of the empty space between OCR boxes.
        # YOUR CODE STARTS HERE
        for box in ocr_boxes:
            # removes all boxes that are out of the table
            if box[0] > (self.top_left_x + self.width) or box[1] < self.top_left_x:
                ocr_boxes.remove(box)

        if len(ocr_boxes) < 2:
            # returns empty list if there are either no or one box within in the table
            return []

        for box in ocr_boxes:
            # appends ending coordinate to boxes
            # doing this after kicking out irrelevant boxes and ending early (see if statement) prevents unnescesarry time
            box.append(box[0] + box[2])

        sep_list = []

        for box in ocr_boxes:
            

        # out put has to be within table and not page!!!!
        # YOUR CODE ENDS HERE


t1 = Table(10, 10, 410, 210)
c1 = t1.calculate_columns([11, 11, 79, 29], [100, 11, 90, 29])
# c1 should be [95]

t2 = Table(10, 10, 410, 210)
c2 = t2.calculate_columns([11, 11, 79, 29], [100, 11, 90, 29], [11, 51, 150, 29])
# c2 should be []
