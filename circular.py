import sys

# Felt it was simpler to add a third attribute previous
class Link(object):
  def __init__(self, data, next=None, previous=None):
    self.data = data
    self.next = next
    self.previous = previous


class CircularList(object):
  # Constructor
  def __init__(self):
    self.first = None

  def insert(self, data):
    newNode = Link(data)
    temp = self.first
    if self.first == None:
      self.first = newNode
      newNode.next = self.first
      newNode.previous = self.first
      self.first = newNode
      return None
    while (temp.next != self.first):
      temp = temp.next
    temp.next = newNode
    newNode.previous = temp
    newNode.next = self.first
    self.first.previous = newNode

  # Find the Link with the given data (value)
  # or return None if the data is not there
  def find(self, data):
    d = self.first
    # Checks to see if link exists
    if (d == None):
      return None

    # Simple linear search to find next person to be eliminated from number via find->delete_after->delete
    while (d.data != data):
      if (d.next == self.first):
        return None
      d=d.next
    return d

  # Delete a Link with a given data (value) and return the Link
  # or return None if the data is not there
  def delete(self, data):
    temp = self.first
    if temp == None:
      return None
    if temp.next != None:
      # if head node is to be deleted
      if (temp.data == data):
        if self.first.next == self.first:
          self.first = None
          return temp
        self.first = temp.next
        temp.next = None
        self.first.previous = temp.previous
        temp.previous = None
        self.first.previous.next = self.first
        return temp
      else:
        while temp.next != self.first:
          if temp.data == data:
            break
          temp = temp.next
        if temp.next and temp.data == data:
          # if element to be deleted is in between
          temp.previous.next = temp.next
          temp.next.previous = temp.previous
          temp.next = None
          temp.previous = None
          return temp
        else:
          return None

    if temp == None:
      return None

  # Delete the nth Link starting from the Link start
  # Return the data of the deleted Link AND return the
  # next Link after the deleted Link in that order
  def delete_after(self, start, n):
    num = self.first
    if (num == None):
      return None
    # Finds starting point for n in the list
    num = self.find(start)
    if num == None:
      return None
    i = 0
    while i < n - 1:
      num = num.next
      i += 1
    num_next = num.next
    self.delete(num.data)
    return num.data, num_next


  def __str__(self):
    temp = self.first
    # if there are no more left to be eliminated or empty list
    if temp == None:
      return "[]"
    out = ""
    # appends the fallen soldiers
    while temp.next != self.first:
      if temp.next != self.first:
        out += str(temp.data) + ", "

      temp = temp.next
    out += str(self.first.previous.data)
    return "[" + out + "]"


def main():
  # read number of soldiers
  line = sys.stdin.readline()
  line = line.strip()
  num_soldiers = int(line)

  # read the starting number
  line = sys.stdin.readline()
  line = line.strip()
  start_count = int(line)

  # read the elimination number
  line = sys.stdin.readline()
  line = line.strip()
  elim_num = int(line)

  # your code
  list = CircularList()

  num = 1
  # Use counter variable instead of for loop so list is appended sequentially instead of backwards
  while num <= num_soldiers:
    list.insert(num)
    num += 1
  dead = 1
  # find Link of start_count
  # Conversely instead of appending the remaining soldiers, appends the fallen soldiers
  elim = []
  while dead <= num_soldiers:
    start_count = list.delete_after(start_count, elim_num)
    elim.append(start_count[0])
    start_count = start_count[1].data
    dead += 1

  # Standard print of all eliminated soldiers
  for item in elim:
    print(item)


if __name__ == "__main__":
  main()
