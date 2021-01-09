
class Property:
    def __init__(self, data):
        self.data = data

    def get_tuple(self):
        tuple_ = tuple((
            self.data['description']['title'],
            self.data['description']['description'],
            None,
            self.data['description']['photo'],
            self.data['description']['contact_name'],
            self.data['description']['contact_phone'],
            None,
            None,
            self.data['property']['type'],
            self.data['property']['city'],
            self.data['property']['district'],
            self.data['property']['sex'],
            self.data['property']['pets'],
            self.data['property']['smoke'],
            self.data['property']['owner'],
            self.data['property']['rooms'],
            self.data['property']['price'],
            42.3525,
            2.4353
        ))
        return str(tuple_).replace('None', 'null')