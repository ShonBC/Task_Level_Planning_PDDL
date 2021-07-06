from industrial_robot import industrial

class ground(industrial):

    def __init__(self, name: str, payload: float, application: list, linear_rail_length: float, company = 'NIST'):
        super().__init__(name, payload, application, company=company)
        self.linear_rail_length = linear_rail_length

    def __str__(self):
        return f'Name: {self._name}, Payload: {self.payload}, Application: {self.application}, Linear Rail Length: {self.linear_rail_length}, Company: {self._company}'

    def discard_part(self, parttype: str):

        print(f'{self._name} discards {parttype}')
if __name__ == '__main__':
    
    gnd = ground('Shon', 2.0, ['s', 'a'], 1.0, 'NIST')
    print(gnd)