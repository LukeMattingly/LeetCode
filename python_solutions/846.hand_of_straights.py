from typing import List
import unittest


class Solution:
    def isNStraightHand(self, hand: List[int], groupSize: int) -> bool:
        if len(hand) % groupSize != 0:
            return False

        totalGroups = len(hand) // groupSize
        hand.sort()

        # Initialize empty groups
        hashmap = {i: [] for i in range(totalGroups)}

        for h in hand:
            placed = False
            for i in range(totalGroups):
                group = hashmap[i]

                # CASE 1: Empty group → can always start a new one
                if not group:
                    group.append(h)
                    placed = True
                    break

                # CASE 2: Can continue a consecutive sequence
                elif len(group) < groupSize and h == group[-1] + 1:
                    group.append(h)
                    placed = True
                    break

                # else: skip group, it can’t accept this card

            # If we couldn’t place this card in any group → fail early
            if not placed:
                return False

        # Finally: verify all groups are full
        return all(len(v) == groupSize for v in hashmap.values())