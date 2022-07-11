import re


def is_vailable(str_to_scann: str) -> int:
    chr_obs = "#"
    chr_hot = "*"
    pattern = "\# *?P *?\#"
    if (chr_obs in str_to_scann):
        if (re.search(pattern, str_to_scann, re.IGNORECASE)):
            return 0
    count_obs = str_to_scann.count(chr_obs)
    count_hots = str_to_scann.count(chr_hot)

    return 0 if(count_hots <= count_obs) else count_hots - count_obs

if __name__ == "__main__":
    str_hack = "***#           P         #***"
    hotsposts = is_vailable(str_hack)
    print("Hotspots vailables:",hotsposts)