import xml.sax
class MovieHandler(xml.sax.ContentHandler):
    def __init__(self):
        self.CurrentData = ""
        self.products = ""
        self.price_type = ""
        self.best_phone = ""
        self.Os = ""
    def startElement(self, tag, attributes):
        # print("Welcome to movies.in\nCheck out the latest information below!")
        print(tag)
        self.CurrentData = tag
        if tag == "phone_name":
            print("******phone*****")
            title = attributes["title"]
            print("Company Name is :{}".format(title))
        else:
            print("Something Wrong Has Happened try again latter")
    def endElement(self, tag):
        if self.CurrentData == "products":
            print("Type of products ", self.products)
        elif self.CurrentData == "price_type":
            print("Price:", self.price_type)
        elif self.CurrentData == "best_phone":
            print("Best phone {}".format(self.best_phone))
        elif self.CurrentData == "Os":
            print("Operating System is ", self.Os)
        self.CurrentData = ""

    def characters(self, content):
        if self.CurrentData == "products":
            self.products = content
        elif self.CurrentData == "price_type":
            self.price_type= content
        elif self.CurrentData == "best_phone":
            self.best_phone = content


if (__name__ == "__main__"):
    # create an XMLReader
    parser = xml.sax.make_parser()
    # turn off namepsaces
    parser.setFeature(xml.sax.handler.feature_namespaces, 0)

    # override the default ContextHandler
    Handler = MovieHandler()
    parser.setContentHandler(Handler)
    parser.parse("pymy.xml")





