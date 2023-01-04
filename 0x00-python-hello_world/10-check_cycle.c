#include "lists.h"

/**
 * check_cycle - checks if a singly linked list has a cycle
 * @list: the list concerned
 * Return: 0 if there is no cycle
 *      1 if there is a cycle
 */
int check_cycle(listint_t *list)
{
	listint_t *fast;
	listint_t *slow;

	fast = list->next;
	slow = list;

	while (fast != NULL && fast->next != NULL && slow != NULL)
	{
		if (fast == slow)
			return (1);

		fast = fast->next->next;
		slow = slow->next;
	}

	return (0);
}
