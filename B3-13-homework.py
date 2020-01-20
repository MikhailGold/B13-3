from B3_13_homework_cls import Tag
from B3_13_homework_cls import HTML
from B3_13_homework_cls import TopLevelTag

def main(output=None):
    with HTML(output=output) as doc:
        with TopLevelTag("head") as head:
            with Tag("title") as title:
                title.text = "Hello example page"
                head += title
            doc += head

        with TopLevelTag("body") as body:
            with Tag("h1", klass=("main-text-example",)) as h1:
                h1.text = "Test"
                body += h1

            with Tag("div", klass=("container", "container-fluid"), id="lead") as div:
                with Tag("p") as paragraph:
                    paragraph.text = "Example text"
                    div += paragraph

                with Tag(
                    "img", is_single=True, src="/example.png", data_image="exmaple_image"
                ) as img:
                    div += img

                body += div

            doc += body
if __name__ == "__main__":
    main("b3-13-example.html")