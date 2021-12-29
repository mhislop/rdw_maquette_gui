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
            True
        )
    )
    traffic_light_sets.append(
        TrafficLightSet(
            1,
            3,
            4,
            5,
            [275, 500],
            True
        )
    )
    traffic_light_sets.append(
        TrafficLightSet(
            2,
            6,
            7,
            8,
            [520, 500],
            True
        )
    )
    traffic_light_sets.append(
        TrafficLightSet(
            3,
            9,
            10,
            11,
            [520, 370],
            True
        )
    )
    traffic_light_sets.append(
        TrafficLightSet(
            4,
            12,
            13,
            14,
            [520, 110],
            True
        )
    )
    traffic_light_sets.append(
        TrafficLightSet(
            5,
            17,
            27,
            22,
            [390, 110],
            False
        )
    )
    traffic_light_sets.append(
        TrafficLightSet(
            6,
            5,
            6,
            13,
            [140, 110],
            False
        )
    )
    traffic_light_sets.append(
        TrafficLightSet(
            7,
            19,
            26,
            18,
            [140, 240],
            False
        )
    )

    return traffic_light_sets
