from image import Search

print(Search(1).getLinks("homeless man"))
print(Search(1).getThumbs("homeless man"))
print(Search(1).getLinksAndThumbs("homeless man"))

"""
EXPECTED OUTCOME
[u'https://cdn.pixabay.com/photo/2014/12/01/10/24/homeless-man-552571_640.jpg']
[u'https://tse2.mm.bing.net/th?id=OIP.-26O8GcnriZiVHHl0P9SMgHaFj&pid=Api']
[Image(thumb=u'https://tse2.mm.bing.net/th?id=OIP.-26O8GcnriZiVHHl0P9SMgHaFj&pid=Api', link=u'https://cdn.pixabay.com/photo/2014/12/01/10/24/homeless-man-552571_640.jpg')]
"""
