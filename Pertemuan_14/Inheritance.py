class Orang:
  def __init__(self, fname, lname):
    self.firstname = fname
    self.lastname = lname

  def tampilnama(self):
    print(self.firstname, self.lastname)

x = Orang("Rafis", "Doe")
x.tampilnama()