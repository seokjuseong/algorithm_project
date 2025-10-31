#======================================================# 
# SW알고리즘 2차 과제 제출                                
# 학번: 20220750                                        
# 이름: 석주성                                           
# 과목: SW알고리즘                                          
#Node 클래스와 LinkedList 클래스 강의코드 활용하였습니다 
#========================================================#
class Node:
    def __init__(self, data, link=None):
        self.data = data
        self.link = link  

    def append(self, new):
        if new is not None:
            new.link = self.link
            self.link = new

    def popNext(self):
        deleted = self.link
        if deleted is not None:
            self.link = deleted.link
            deleted.link = None
        return deleted


class LinkedList:
    def __init__(self):
        self.head = None

    def isEmpty(self):
        return self.head is None

    def append(self, book):
        new_node = Node(book)
        if self.isEmpty():
            self.head = new_node
        else:
            ptr = self.head
            while ptr.link is not None:
                ptr = ptr.link
            ptr.link = new_node

    def getNode(self, pos):
        # pos번째에 있는 노드를 반환하기
        # 리스트의 인덱스는 0부터 시작
        if pos < 0 : return None # pos는 invalid 졍우
        if self.head == None: # 주어진 리스트가 공백
            return None
        else:
            ptr  = self.head
            for _ in range(pos):
                if ptr == None: # pos가 리스트 크기보다 큰 경우 
                    return None
                ptr = ptr.link # 링크따라 이동
            return ptr #pos에 있는 노드 반환

    def find_by_title(self, title):
        ptr = self.head
        while ptr is not None:
            if ptr.data.title == title:
                return ptr.data 
            ptr = ptr.link
        return None  

    
    def find_pos_by_title(self, title):
        ptr = self.head
        pos = 0
        while ptr is not None:
            if ptr.data.title == title:
                return pos  # 
            ptr = ptr.link
            pos += 1
        return -1  

    def delete(self, pos):
        if pos < 0:
            raise IndexError("empty 또는 리스트 범위 밖 오류")
        
        before = self.getNode(pos-1)  # 삭제할 노드 이전 노드

        if before is None:
            if pos == 0:  # 머리 노드 삭제
                deleted = self.head
                self.head = deleted.link
                deleted.link = None
                return deleted
            else:  # pos가 리스트 범위 밖
                raise ValueError("리스트 범위 밖 오류")
        else:
            return before.popNext()  # 중간/끝 노드 삭제

            



class Book:
    def __init__(self, num, title, author, year):
        self.num = num
        self.title = title
        self.author = author
        self.year = year


class BookManagement:
    def __init__(self):
        self.book_list = LinkedList() #연결리스트 만들기

    def add_book(self, book_id, title, author, year):
        ptr = self.book_list.head
        while ptr is not None: #책번호가 존재하거나, 책 제목이 중복되는경우 리스트에 추가를하지않고 반환 
            if ptr.data.num == book_id:
                print(f"오류: 이미 존재하는 도서 번호 '{book_id}'입니다.")
                return
            if ptr.data.title == title:
                print(f"오류: 이미 존재하는 도서 제목 '{title}'입니다.")
                return
            ptr = ptr.link

        book = Book(book_id, title, author, year)
        self.book_list.append(book)
        print(f"'{title}' 도서가 추가되었습니다.")

    def remove_book(self, title):
        pos = self.book_list.find_pos_by_title(title)  # 제목에 해당하는 위치를 find_pos_by_title메소드를 이용해 위치를 찾습니다. 
        if pos == -1: #제목에 해당하는 리스트가 존재하지않는다면 
            print("해당 제목의 도서를 찾을 수 없습니다.")
            return
    
        deleted_node = self.book_list.delete(pos)  # delte(pos) 내에서 popnext 호출해서 삭제작업 진행.
        print(f"'{deleted_node.data.title}' 도서가 삭제되었습니다.")

    def search_book(self, title):
        book = self.book_list.find_by_title(title) #Linkedlist 클래스내의 find_by_title메소드를 이용하여 해당 제목을 가진 책을 가져옵니다.
        if book:
            print(f"\n=== 도서 정보 ===\n번호: {book.num}\n제목: {book.title}\n저자: {book.author}\n출판년도: {book.year}")
        else: #None 인경우
            print("해당 제목의 도서를 찾을 수 없습니다.")


    def display_books(self):
        if self.book_list.isEmpty(): #리스트가 None인경우
            print("현재 등록된 도서가 없습니다.")
            return
        ptr = self.book_list.head
        print("\n=== 전체 도서 목록 ===")
        while ptr is not None:
            book = ptr.data
            print(f"번호: {book.num}, 제목: {book.title}, 저자: {book.author}, 출판년도: {book.year}")
            ptr = ptr.link


    def run(self):
            while True:
                print("""
    === 도서 관리 프로그램 ===
    1. 도서 추가
    2. 도서 삭제 (책 제목으로 삭제)
    3. 도서 조회 (책 제목으로 조회)
    4. 전체 도서 목록 출력
    5. 종료
    """)
                choice = input("메뉴를 선택하세요: ")

                if choice == "1":
                    num = input("도서 번호: ")
                    title = input("도서 제목: ")
                    author = input("저자: ")
                    year = input("출판년도: ")
                    self.add_book(num, title, author, year)

                elif choice == "2":
                    title = input("삭제할 도서 제목: ")
                    self.remove_book(title)

                elif choice == "3":
                    title = input("조회할 도서 제목: ")
                    self.search_book(title)

                elif choice == "4":
                    self.display_books()

                elif choice == "5":
                    print("프로그램을 종료합니다.")
                    break

                else:
                    print("잘못된 입력입니다. 다시 선택해주세요.")


if __name__ == "__main__":
    m = BookManagement()
    m.run()
