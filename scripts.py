def all_activities_to_list(activities):
    activity_list = list(activities)  
    final_list=[]

    for activity in activity_list:
        activities_list = {
            'id' : activity.id,
            'name' : activity.name,
            'id' : activity.id,
            'name' : activity.name,
            'distance' : activity.distance,
            'moving_time' : activity.moving_time,
            'elapsed_time' : activity.elapsed_time,
            'total_elevation_gain' : activity.total_elevation_gain,
            'type' : activity.type,
            'sport_type' : activity.sport_type,
            'start_date' : activity.start_date,
            'start_date_local' : activity.start_date_local,
            'timezone' : activity.timezone,
            'location_city' : activity.location_city,
            'location_state' : activity.location_state,
            'location_country' : activity.location_country,
            'achievement_count' : activity.achievement_count,
            'kudos_count' : activity.kudos_count,
            'comment_count' : activity.comment_count,
            'athlete_count' : activity.athlete_count,
            'photo_count' : activity.photo_count,
            'map' : activity.map,
            #'trainer' : activity.trainer,
            #'commute' : activity.commute,
            #'manual' : activity.manual,
            #'private' : activity.private,
            #'visibility' : activity.visibility,
            #'flagged' : activity.flagged,
            'workout_type' : activity.workout_type,
            #'device_watts' : activity.device_watts,
            'average_speed' : activity.average_speed,
            'max_speed' : activity.max_speed,
            #'average_cadence' : activity.average_cadence,
            #'average_watts' : activity.average_watts,
            #'weighted_average_watts' : activity.weighted_average_watts,
            #'kilojoules' : activity.kilojoules,    
            #'gear_id' : activity.gear_id,  
        }
        final_list.append(activities_list)
    return final_list