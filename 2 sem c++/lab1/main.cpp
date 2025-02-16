#include <iostream>
#include <string>
#include <sstream>

struct Node {
    int data;      
    Node* prev;   
    Node* next;    

    Node(int val = 0) : data(val), prev(nullptr), next(nullptr) {}
};

class DoublyLinkedCyclicList {
private:
    Node* head;    

public:
    DoublyLinkedCyclicList() {
        head = new Node();      
        head->next = head;      
        head->prev = head;      
    }

    ~DoublyLinkedCyclicList() {
        clear();
        delete head;
    }

    void clear() {
        Node* current = head->next;
        while (current != head) {
            Node* temp = current;
            current = current->next;
            delete temp;
        }
        head->next = head;
        head->prev = head;
    }

    bool empty() {
        return head->next == head;
    }

    void push_back(int val) {
        Node* newNode = new Node(val);
        newNode->prev = head->prev;
        newNode->next = head;
        head->prev->next = newNode;
        head->prev = newNode;
    }

    void erase(Node* node) {
        if (node == head) return; 
        node->prev->next = node->next;
        node->next->prev = node->prev;
        delete node;
    }

    Node* getHead() {
        return head;
    }

    void print() {
        Node* current = head->next;
        while (current != head) {
            std::cout << current->data << ' ';
            current = current->next;
        }
        std::cout << '\n';
    }
};

int firstDigit(int n) {
    while (n >= 10)
        n /= 10;
    return n;
}

int lastDigit(int n) {
    return n % 10;
}

bool isOrderedNonDecreasingByFirstDigit(DoublyLinkedCyclicList& list) {
    Node* current = list.getHead()->next;
    Node* head = list.getHead();

    if (current == head || current->next == head)
        return true; 

    while (current->next != head) {
        int currentFirstDigit = firstDigit(current->data);
        int nextFirstDigit = firstDigit(current->next->data);
        if (nextFirstDigit < currentFirstDigit) {
            return false; 
        }
        current = current->next;
    }
    return true; 
}

bool isOrderedNonDecreasingByLastDigit(DoublyLinkedCyclicList& list) {
    Node* current = list.getHead()->next;
    Node* head = list.getHead();

    if (current == head || current->next == head)
        return true; 

    while (current->next != head) {
        int currentLastDigit = lastDigit(current->data);
        int nextLastDigit = lastDigit(current->next->data);
        if (nextLastDigit < currentLastDigit) {
            return false; 
        }
        current = current->next;
    }
    return true; 
}

bool consistsOfDigits1to5(int n) {
    if (n == 0)
        return false; 
    while (n > 0) {
        int digit = n % 10;
        if (digit < 1 || digit > 5)
            return false; 
        n /= 10;
    }
    return true; 
}

bool containsDigit6or8(int n) {
    while (n > 0) {
        int digit = n % 10;
        if (digit == 6 || digit == 8)
            return true; 
        n /= 10;
    }
    return false; 
}


void sortListDesc(DoublyLinkedCyclicList& list) {
    Node* head = list.getHead();
    if (head->next == head || head->next->next == head)
        return; 

    bool swapped;
    do {
        swapped = false;
        Node* current = head->next;
        while (current->next != head) {
            if (current->data < current->next->data) {
                int temp = current->data;
                current->data = current->next->data;
                current->next->data = temp;
                swapped = true;
            }
            current = current->next;
        }
    } while (swapped);
}


int main() {
    DoublyLinkedCyclicList list;  

    std::cout << "Enter a sequence of natural numbers:\n";
    std::string line;
    std::getline(std::cin, line); 
    std::istringstream iss(line);
    int num;
    while (iss >> num) {
        if (num > 0) { 
            list.push_back(num); 
        } else {
            std::cout << "Please enter natural numbers only.\n";
            return 1;
        }
    }

    bool orderedByFirstDigit = isOrderedNonDecreasingByFirstDigit(list);
    bool orderedByLastDigit = isOrderedNonDecreasingByLastDigit(list);

    if (orderedByFirstDigit || orderedByLastDigit) {
        Node* head = list.getHead();
        Node* current = head->next;

        while (current != head) {
            Node* nextNode = current->next; 

            int data = current->data;

            if (consistsOfDigits1to5(data)) {
                list.erase(current);
            } else if (containsDigit6or8(data)) {
                Node* newNode = new Node(data);
                newNode->prev = current;
                newNode->next = current->next;
                current->next->prev = newNode;
                current->next = newNode;
            }
            current = nextNode;
        }
    } else {
        sortListDesc(list);
    }

    std::cout << "Processed sequence:\n";
    list.print();

    return 0;
}
