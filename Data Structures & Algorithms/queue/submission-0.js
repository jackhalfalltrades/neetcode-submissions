class Node {
    constructor(val, nextNode= null, prevNode = null) {
        this.val = val
        this.next = nextNode
        this.prev = prevNode
    }
}


class Deque {
    constructor() {
        this.head = new Node(-1, null, null)
        this.tail = new Node(-1, null, null)
        this.head.next = this.tail
        this.tail.prev = this.head
    }

    /**
     * @return {boolean}
     */
    isEmpty() {
        if(this.head.next === this.tail) {
            return true
        } return false
    }

    /**
     * @param {number} value
     */
    append(value) {
        const node = new Node(value, this.tail, this.tail.prev)
        this.tail.prev.next =node
        this.tail.prev = node
    }

    /**
     * @param {number} value
     * @return {void}
     * nextNode= null, prevNode = null
     */
    appendleft(value) {
        const node = new Node(value, this.head.next, this.head)
        this.head.next.prev = node
        this.head.next = node
    }

    /**
     * @return {void}
     */
    pop() {
        if(this.isEmpty()) {
            return -1
        }
        const node = this.tail.prev
        this.tail.prev.prev.next = this.tail
        this.tail.prev = this.tail.prev.prev
        return node.val
    }

    /**
     * @return {number}
     */
    popleft() {
        if(this.isEmpty()) {
            return -1
        }
        const node = this.head.next
        this.head.next.next.prev = this.head
        this.head.next = node.next
        return node.val
    }
}
