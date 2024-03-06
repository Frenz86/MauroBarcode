import cv2
from pyzbar import pyzbar

def draw_barcode(decoded, image):
    image_with_rect = cv2.rectangle(image, (decoded.rect.left, decoded.rect.top), 
                            (decoded.rect.left + decoded.rect.width, decoded.rect.top + decoded.rect.height),
                            color=(0, 255, 0),
                            thickness=5)
    # Crop the image using the rectangle coordinates
    cropped_image = image_with_rect[decoded.rect.top:decoded.rect.top + decoded.rect.height,
                                    decoded.rect.left:decoded.rect.left + decoded.rect.width]
    return cropped_image


def decode(image):
    # decodes all barcodes from an image
    decoded_objects = pyzbar.decode(image)
    for obj in decoded_objects:
        # draw the barcode
        print("detected barcode:", obj)
        image = draw_barcode(obj, image)
        # print barcode type & data
        print("Type:", obj.type)
        print("Data:", obj.data)
        print()
    return image

def barcode(image):
    # decodes all barcodes from an image
    decoded_objects = pyzbar.decode(image)
    barcode = []
    for obj in decoded_objects:
        barcode.append(obj.data)
    return barcode

img = cv2.imread("test.jpg")
# decode detected barcodes & get the image
print(barcode(img))
img = decode(img)
# show the image
cv2.imshow("img", img)
cv2.waitKey(0)