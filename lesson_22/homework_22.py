from pathlib import Path
from playwright.sync_api import sync_playwright

URL = "https://qauto2.forstudy.space/"
LOGIN = "guest"
PASSWORD = "welcome2qauto"


def extract_locators(page):
    
    elements = page.query_selector_all("*")[:25]

    locators = []
    for i, el in enumerate(elements, start=1):
        tag = el.evaluate("el => el.tagName.toLowerCase()")
        
       
        css = f"{tag}:nth-of-type({i})"
      
        xpath = el.evaluate("""
            el => {
                function getXPath(element) {
                    if (element.id!=='')
                        return 'id(\"'+element.id+'\")';
                    if (element===document.body)
                        return '/html/body';
                    let ix=0;
                    let siblings=element.parentNode.childNodes;
                    for (let i=0;i<siblings.length;i++){
                        let sib=siblings[i];
                        if(sib===element) return getXPath(element.parentNode)+'/'+element.tagName.toLowerCase()+'['+(ix+1)+']';
                        if(sib.nodeType===1 && sib.tagName===element.tagName) ix++;
                    }
                }
                return getXPath(el);
            }
        """)

        locators.append(f"{i}. CSS: {css}")
        locators.append(f"   XPath: {xpath}\n")

    return locators


def save_to_file(locators):
    script_dir = Path(__file__).parent
    file_path = script_dir / "locators.txt"

    with open(file_path, "w", encoding="utf-8") as f:
        for line in locators:
            f.write(line + "\n")

    print(f"Файл збережено: {file_path}")


def main():
    with sync_playwright() as p:
        browser = p.chromium.launch(headless=True)  # headless=True – без вікна браузера
        context = browser.new_context(http_credentials={"username": LOGIN, "password": PASSWORD})
        page = context.new_page()
        page.goto(URL)

       
        page.wait_for_selector("app-root")  

        locators = extract_locators(page)
        save_to_file(locators)

        browser.close()


if __name__ == "__main__":
    main()