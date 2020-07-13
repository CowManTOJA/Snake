def check_img_size(img, size):
    if size != img.get_rect().size:
        raise Exception(f'Picture need to be {size[0]}x{size[1]}px')

    return img
