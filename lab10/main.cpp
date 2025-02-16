#include <iostream>
#include <sstream> 

class Node {
public:
    double data;
    Node* next;

public:
    Node(double data) {
        this->data = data;
        this->next = NULL;
    }
};

class OneLinkedList {
public:
    Node* head, * tail;
public:
    OneLinkedList() {
        this->head = this->tail = NULL;
    }
    ~OneLinkedList() {
        while (head != NULL) pop_front();
    }

    void pop_front() {
        if (head == NULL) return;
        if (head == tail) {
            delete tail;
            head = tail = NULL;
            return;
        }

        Node* node = head;
        head = node->next;
        delete node;
    }

    void push_back(double data) {
        Node* node = new Node(data);
        if (head == NULL) head = node;
        if (tail != NULL) tail->next = node;
        tail = node;
    }

    void push_front(double data) {
        Node* node = new Node(data);
        node->next = head;
        head = node;
        if (tail == NULL) tail = node;
    }

    void print() {
        Node* current = head;
        while (current != NULL) {
            std::cout << current->data << " ";
            current = current->next;
        }
        std::cout << std::endl;
    }

    bool hasThreeDigitOdd() {
        Node* current = head;
        while (current != NULL) {
            int num = static_cast<int>(current->data);
            if (num >= 100 && num < 1000) {
                if ((num % 2 != 0) && (num % 10 % 2 != 0) && ((num / 10) % 10 % 2 != 0)) {
                    return true;
                }
            }
            current = current->next;
        }
        return false;
    }

    void sortByFirstDigit() {
        if (head == NULL || head->next == NULL) return; //-

        bool swapped;
        do {
            swapped = false;
            Node* current = head;
            while (current->next != NULL) {
                int firstDigitA = static_cast<int>(current->data);
                while (firstDigitA >= 10) firstDigitA /= 10;
                int firstDigitB = static_cast<int>(current->next->data);
                while (firstDigitB >= 10) firstDigitB /= 10;

                if (firstDigitA < firstDigitB) {
                    std::swap(current->data, current->next->data);
                    swapped = true;
                }
                current = current->next;
            }
        } while (swapped);
    }

    void filterAndDuplicate() {
        Node* current = head;
        OneLinkedList newList;

        while (current != NULL) {
            int num = static_cast<int>(current->data);
            if (std::to_string(num).find('8') != std::string::npos) {
                newList.push_back(current->data);
                newList.push_back(current->data); 
            }
            current = current->next;
        }

        while (head != NULL) pop_front();
        head = newList.head;
        tail = newList.tail;
        newList.head = newList.tail = NULL; 
    }
};

int main() {
    OneLinkedList lst;
    int n;
    std::cout << "Enter number of elements: ";
    std::cin >> n;

    std::cout << "Enter numbers: ";
    for (int i = 0; i < n; ++i) {
        double num;
        std::cin >> num;
        lst.push_back(num);
    }

    if (!lst.hasThreeDigitOdd()) {
        lst.sortByFirstDigit();
    } else {
        lst.filterAndDuplicate();
    }

    std::cout << "Result: ";
    lst.print();

    return 0;
}