import time

def highlight(element):
    """Highlights (blinks) a Selenium Webdrddfiver element"""
    driver = element._parent
    def apply_style(s):
        driver.execute_script("arguments[0].setAttribute('style', arguments[1]);",
                              element, s)
    original_style = element.get_attribute('style')
    apply_style("background: blue; border: 5px solid black;")
    time.sleep(.6)
    apply_style(original_style)