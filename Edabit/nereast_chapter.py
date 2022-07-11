def nearest_chapter(dates_dict : dict, num_page: int) -> str:
    for key, value in dates_dict.items():
        dates_dict.update({key : abs(value - num_page) })
    
    dates_dict = sorted(dates_dict.items(), key = lambda x: x[1])
    return dates_dict[0][0]


if __name__ == "__main__":
    dictionary = {"Chapter 1a" : 1,"Chapter 1b" : 5}
    page = 3
    chapter_nest = nearest_chapter(dictionary, page)
    print("Chapter nest:", chapter_nest)