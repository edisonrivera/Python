from re import IGNORECASE, findall


def extract_all(html_code: str):
    pattern_opening = "<[a-z]+>"
    opening_tags = findall(pattern_opening, html_code, IGNORECASE)

    pattern_closing = "<\/[a-z]+>"
    closing_tags = findall(pattern_closing, html_code, IGNORECASE)

    pattern_tag_content = "<\/?[a-z]+>(?:.*(?:<\/[a-z]+>)?(?:.+)?(?:<\/[a-z]+)?>)?"
    all_tags = findall(pattern_tag_content, html_code,IGNORECASE)

    return opening_tags, closing_tags, all_tags


if __name__ == "__main__":
    code = '''
        <html>
        <head>
            Hi! I'm a text in the head.
            I probably shouldn't be here.
            <title>edabit.com</title>
        </head>
        <body>
            Hi! I'm a text in the body.
            <p>This is a parragraph and <a href="https://edabit.com">this is a link</a>.</p>
            Here comes a fake tag: <>.
        </body>
        </html>
    '''

    opening_tags, closing_tags, all_tags = extract_all(code)
    print("Opening tags:", opening_tags, "\nClosing Tags:", closing_tags, "\nAll tags:", all_tags)