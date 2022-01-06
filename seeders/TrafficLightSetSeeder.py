from classes.TrafficLightSet import TrafficLightSet

def TrafficLightSetSeeder():
    traffic_light_sets = []
    traffic_light_sets.append(
        TrafficLightSet(
            0,
            0,
            1,
            2,
            [140, 500],
            True,
            [0, 4]
        )
    )
    traffic_light_sets.append(
        TrafficLightSet(
            1,
            3,
            4,
            5,
            [275, 500],
            True,
            [1,5]
        )
    )
    traffic_light_sets.append(
        TrafficLightSet(
            2,
            6,
            7,
            15,
            [520, 500],
            True,
            [2,6]
        )
    )
    traffic_light_sets.append(
        TrafficLightSet(
            3,
            14,
            13,
            12,
            [520, 370],
            True,
            [3,7]
        )
    )
    traffic_light_sets.append(
        TrafficLightSet(
            4,
            11,
            10,
            9,
            [520, 110],
            True,
            [0,4]
        )
    )
    traffic_light_sets.append(
        TrafficLightSet(
            5,
            17,
            27,
            22,
            [390, 110],
            False,
            [1,5]
        )
    )
    traffic_light_sets.append(
        TrafficLightSet(
            6,
            13,
            6,
            5,
            [140, 110],
            False,
            [2,6]
        )
    )
    traffic_light_sets.append(
        TrafficLightSet(
            7,
            19,
            26,
            18,
            [140, 240],
            False,
            [3,7]
        )
    )

    return traffic_light_sets
