#include "lists.h"

/**
 * check_cycle - looks for a cycle on a single linked list
 * @list: Pointer to list's head
 * Return: 1 if a cycle is found, 0 otherwise
 */

int check_cycle(listint_t *list)
{
	listint_t *slow, *fast;

	slow = list;
	fast = list;
	while (slow && fast)
	{
		slow = slow->next;
		fast = fast->next;
		if (fast)
			fast = fast->next;
		if (slow && fast && slow == fast)
			return (1);
	}
	return (0);
}