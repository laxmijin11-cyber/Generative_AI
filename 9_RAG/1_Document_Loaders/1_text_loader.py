from langchain_community.document_loaders import TextLoader

# object of TextLoader class
# imp parameter is path
loader = TextLoader("cricket.txt", encoding="utf-8")

docs = loader.load()
# print(docs)
"""
[Document(metadata={'source': 'cricket.txt'}, page_content="Cricket is a bat-and-ball game that is played between two teams of eleven players on a field, at the centre of which is a 22-yard (20-metre; 66-foot) pitch with a wicket at each end, each comprising two bails (small sticks) balanced on three stumps. Two players from the batting team, the striker and nonstriker, stand in front of either wicket holding bats, while one player from the fielding team, the bowler, bowls the ball toward the striker's wicket fromthe opposite end of the pitch. The striker's goal is to hit the bowled ball with the bat and then switch places with the nonstriker, with the batting team scoring one run for each of these swaps. Runs are also scored when the ball reaches the boundary of the field or when the ball is bowled illegally.")]
<class 'list'>
"""

# print(type(docs))
# print(len(docs))

# print(docs[0])

"""
page_content='Cricket is a bat-and-ball game that is played between two teams of eleven players on a field, at the centre of which is a 22-yard (20-metre; 66-foot) pitch with a wicket at each end, each comprising two bails (small sticks) balanced on three stumps. Two players from the batting team, the striker and nonstriker, stand in front of either wicket holding bats, while one player from the fielding team, the bowler, bowls the ball toward the striker's wicket from the opposite end of the pitch. The striker's goal is to hit the bowled ball with the bat and thenswitch places with the nonstriker, with the battingteam scoring one run for each of these swaps. Runs are also scored when the ball reaches the boundary of the field or when the ball is bowled illegally.' metadata={'source': 'cricket.txt'}
"""
# print(type(docs[0]))
# <class 'langchain_core.documents.base.Document'>

# document object
print(docs[0].page_content)
print(docs[0].metadata)


# doc load as list of document load karta hai
