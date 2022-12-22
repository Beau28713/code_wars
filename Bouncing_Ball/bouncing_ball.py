def bouncing(h, bounce, window):
    mom_see = 0
    if h and bounce > 0 and bounce < 1 and window < h:
        mom_see += 1
        while h > window:
            h = calc_bounce_height(h, bounce)
            if h > window:
                mom_see += 2   

        return mom_see

    else:
        return -1

def calc_bounce_height(h, bounce):
    bounce_height = h * (bounce)

    return bounce_height