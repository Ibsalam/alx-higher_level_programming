#include "lists.h"

/**
 * check_cycle - function that checks if a list has a cycle
 * @list : linked list
 * Return : 1 if there is a cycle, 0 if not
 */
int check_cycle(listint_t *list)
{
	listint_t *slow_ptr = list, *fast_ptr = list;

	if (list == NULL || list->next == NULL)
		return (0);

	while (fast_ptr != NULL && fast_ptr->next != NULL)
	{
		slow_ptr = slow_ptr->next;
		fast_ptr = fast_ptr->next->next;

		if (slow_ptr == fast_ptr)
			return (1);
	}

	return (0);
}
