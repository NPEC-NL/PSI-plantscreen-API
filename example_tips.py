import datetime
from os import getenv
from dotenv import load_dotenv

import plantscreen


if __name__ == "__main__":
    """Example implementation of some convenience functions

    Uses the latest experiment.

    The model classes have auto-generated properties that lazy-load related
    objects by calling the appropriate API endpoint automatically.
    These are generated from x-pp-link annotations in the OpenAPI spec.
    Instead of manually calling api.round_experiment(experiment_id), you can
    access experiment.rounds directly.
    """
    load_dotenv()
    # Create an instance of the API class
    api = plantscreen.CompleteAPIClient(getenv("HOST"))

    # Retrieve a list with all experiments
    experiment_list = api.experiment_id()
    experiment_id = experiment_list[-1]

    # --- x-pp-link property examples ---

    # Fetch the experiment object once
    experiment = api.experiment(experiment_id)

    # Instead of: round_list = api.round_experiment(experiment_id)
    # Use the linked property directly on the experiment object:
    round_list = experiment.rounds
    print(f"Rounds for experiment {experiment_id}: {[r.round_id for r in round_list]} \n")

    # Navigate further: each Round also has linked properties
    last_round = round_list[-1]

    # Instead of: api.action_protocol_round(last_round.round_id)
    action_protocol = last_round.action_protocol
    print(f"Action protocol for last round: {action_protocol} \n")

    # Instead of: api.tray_round(last_round.round_id)
    trays = last_round.trays
    print(f"Trays in last round: {[t.tray_id for t in trays]} \n")

    # Each Tray also links to its plants
    if trays:
        first_tray = trays[0]
        # Instead of: api.plant_tray(first_tray.tray_id)
        plants = first_tray.plants
        print(f"Plants on tray {first_tray.tray_id}: {[p.plant_id for p in plants]} \n")

        # Each Plant links to its reference weight
        if plants:
            first_plant = plants[0]
            # Instead of: api.scales_weight_reference_plant(first_plant.plant_id)
            ref_weight = first_plant.reference_weight
            print(f"Reference weight for plant {first_plant.plant_id}: {ref_weight} \n")

    # ID fields also expose their linked object — e.g. on a Round:
    # Instead of: api.experiment(last_round.experiment_id)
    linked_experiment = last_round.experiment
    print(f"Experiment linked from round: {linked_experiment.experiment_name} \n")

    # --- x-pp-rel method examples ---
    # Unlike x-pp-link (no-arg cached properties), x-pp-rel generates methods
    # that accept extra parameters (e.g. date ranges). The ID fields of the
    # object are passed automatically; you only supply the extra arguments.

    start = datetime.datetime(year=2024, month=1, day=1)
    stop = datetime.datetime.now()

    # Experiment.rounds_by_date(start, stop)
    # Instead of: api.round_date_experiment(experiment_id, start, stop)
    rounds_in_range = experiment.rounds_by_date(start, stop)
    round_ids = [r.round_id for r in rounds_in_range]
    print(f"Rounds between {start.date()} and {stop.date()}: {round_ids} \n")

    # Experiment.round_orders_by_date(start, stop)
    # Instead of: api.round_order_date_experiment(experiment_id, start, stop)
    round_orders_in_range = experiment.round_orders_by_date(start, stop)
    print(f"Round orders in range: {round_orders_in_range} \n")

    # Round.system_logs_by_daterange(start, stop)
    # Instead of: api.system_log_date_round(last_round.round_id, start, stop)
    round_logs = last_round.system_logs_by_daterange(start, stop)
    print(f"System logs for last round in range: {round_logs} \n")

    if trays:
        first_tray = trays[0]

        # Tray.tray_profile_used_by_daterange(start, stop)
        # Instead of: api.tray_profile_used_tray(first_tray.tray_id, start, stop)
        tray_profiles = first_tray.tray_profile_used_by_daterange(start, stop)
        print(f"Tray profiles used in range: {tray_profiles} \n")

        # Tray.tray_profile_used_at_time(date) — single-value variant
        # Instead of: api.tray_profile_to_date_tray(first_tray.tray_id, date)
        tray_profile_now = first_tray.tray_profile_used_at_time(stop)
        print(f"Tray profile active now: {tray_profile_now} \n")

        # Tray.plants_by_daterange(start, stop)
        # Instead of: api.plant_tray_profile_tray(first_tray.tray_id, start, stop)
        plants_in_range = first_tray.plants_by_daterange(start, stop)
        print(f"Plants on tray in range: {[p.plant_id for p in plants_in_range]} \n")

        # Tray.system_logs_by_daterange(start, stop)
        # Instead of: api.system_log_date_tray(first_tray.tray_id, start, stop)
        tray_logs = first_tray.system_logs_by_daterange(start, stop)
        print(f"System logs for tray in range: {tray_logs} \n")
