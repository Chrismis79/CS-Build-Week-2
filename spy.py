# In a city-state of n people, there is a rumor going around that one of the n people is a spy for the neighboring city-state.

# The spy, if it exists:
# Does not trust anyone else.
# Is trusted by everyone else (he's good at his job).
# Works alone
# there are no other spies in the city-state.
# You are given a list of pairs, trust. Each trust[i] = [a, b] represents the fact that person a trusts person b.

# BASICALLY LOOKING FOR THE PERSON THE DOESN'T TRUST ANYONE AND EVERYONE TRUSTS THEM.

# If the spy exists and can be found, return their identifier. Otherwise, return -1.

# Example 1:

# Input: n = 2, trust = [[1, 2]]
# Output: 2
# Explanation: Person 1 trusts Person 2, but Person 2 does not trust Person 1, so Person 2 is the spy.
# Example 2:

# Input: n = 3, trust = [[1, 3], [2, 3]]
# Output: 3
# Explanation: Person 1 trusts Person 3, and Person 2 trusts Person 3, but Person 3 does not trust either Person 1 or Person 2. Thus, Person 3 is the spy.
# Example 3:

# Input: n = 3, trust = [[1, 3], [2, 3], [3, 1]]
# Output: -1
# Explanation: Person 1 trusts Person 3, Person 2 trusts Person 3, and Person 3 trusts Person 1. Since everyone trusts at least one other person, there is no spy.
# Example 4:

# Input: n = 3, trust = [[1, 2], [2, 3]]
# Output: -1
# Explanation: Person 1 trusts Person 2, and Person 2 trusts Person 3. However, in this situation, we don't have any one person who is trusted by everyone else. So we can't determine who the spy is in this case.
# Example 5:

# Input: n = 4, trust = [[1, 3], [1, 4], [2, 3], [2, 4], [4, 3]]
# Output: 3
# Explanation: Person 1 trusts Person 3 and Person 4, Person 2 trusts Person 3 and Person 4, Person 4 trusts Person 3. Everyone trusts Person 3 but Person 3 does not trust anyone, so they are the spy.


# PLANNING:
# Spies are identified with three different criteria.
# They do not trust anyone
# They are trusted by everyone else
# They work alone. There are no other spies.

# 1 and 2 should have their own dictionaries. The first dictionary shows who(the key) trusts who(the values). So we iterate over the pairs and add each second value to a list where the first value is the key. So the key value pairs for this:
# [[1, 3],
#  [1, 4],
#  [2, 3],
#  [2, 4],
#  [4, 3]]
# should look like
# {1: [3, 4],
#  2: [3, 4],
#  4: [3]}
# The same is done but in reverse for the second dictionary, getting who is trusted by who.
# For the same key value pairs above, the dict should look like
# {3: [1, 2, 4],
#  4: {1, 2}, }
# figure out who is trusted by everyone else by looking in the second dictionary, and determining who has a value with a length of n-1, n being the number of people in the city.
# Then you can see if that person with the n-1 values is not in the first dictionary.
# If only one person applies to both of these criteria, you have your spy.
# 12: 49
# And of course if you dont find anyone who fills that criteria, you can't determine a spy and you return -1.

n = 4
trust = [[1, 3], [1, 4], [2, 3], [2, 4], [4, 3]]


def uncover_spy(n, trust):
    #
    trusts_dict = {}
    is_trusted_dict = {}

    # loop over trust
    for pair in trust:
        # if each pair not in trusts_dict:
        if pair[0] not in trusts_dict:
            # Assign person x trusts person y to trusts_dict.
            trusts_dict[pair[0]] = [pair[1]]
            print('0', trusts_dict[pair[0]])
        else:
            trusts_dict[pair[0]].append(pair[1])
            print('trusts', trusts_dict)

        # Assigns person y is trusted by person x to is_trusted_dict
        if pair[1] not in is_trusted_dict:
            is_trusted_dict[pair[1]] = [pair[0]]
        else:
            print(is_trusted_dict[pair[1]])
            is_trusted_dict[pair[1]].append(pair[0])
            print('is', is_trusted_dict)

    for key, value in is_trusted_dict.items():
        if key not in trusts_dict and len(value) == n-1:
            return key
    # not found

    return -1


print(uncover_spy(n, trust))
# runtime O(n)
# Improvements:
