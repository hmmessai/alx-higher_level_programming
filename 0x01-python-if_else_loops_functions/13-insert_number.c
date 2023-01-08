#include "lists.h"
#include <stdlib.h>

/**
 *
 */

listint_t *insert_node(listint_t **head, int number)
{
	listint_t *node = *head;
	listint_t *new;

	new = malloc(sizeof(listint_t));
	if (new == NULL)
		return (NULL);

	new->n = number;

	if (node == NULL || node->n >= number)
	{
		new->next = node;
		*head = new;
		return (new);
	}
	
	while (node->next->n < number && node->next && node)
		node = node->next;

	new->next = node->next;
	node->next = new;

	return (new);

}
