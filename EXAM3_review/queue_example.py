class Queue(list):
      def __init__(self):
          list.__init__(self)

      def enQueue(self, item):
          # line should be??
          pass

      def deQueue(self):
          return self.pop(0)



































'''
 39 what should I add for the init ?
     we know because Queue is inherited from a list, we absolutely need to call
     the list constructor, there are  passed in values in the Queue's constructor so,
     we don't need to assign attributes
     ANSWER: list.__init__(self)

'''
'''
 40 what should i add for enQueue?
    this should add whatever passed in item to the end of my queue
    i know that list's have a method that adds elements to the end of my collection
    here I'd take advantage of the way deQueue is written.
    ANSWER: self.append(item)
'''












'''

self.append(item)
'''
