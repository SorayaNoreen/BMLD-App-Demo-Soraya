from datetime import datetime, timedelta

def create_training_plan(race_date, start_date):
    plan = []
    current_date = start_date
    weeks_to_race = (race_date - start_date).days // 7

    for week in range(weeks_to_race):
        week_plan = {
            'week': week + 1,
            'days': []
        }
        for day in range(7):
            day_plan = {
                'date': current_date.strftime('%Y-%m-%d'),
                'workout': ''
            }
            if day == 0:  # Monday
                day_plan['workout'] = 'Rest'
            elif day in [1, 3, 5]:  # Tuesday, Thursday, Saturday
                day_plan['workout'] = 'Run 5-10 km'
            elif day in [2, 4]:  # Wednesday, Friday
                day_plan['workout'] = 'Cross-training'
            else:  # Sunday
                day_plan['workout'] = 'Long run 10-20 km'
            week_plan['days'].append(day_plan)
            current_date += timedelta(days=1)
        plan.append(week_plan)
    
    return plan

race_date = datetime(2025, 4, 13)
start_date = datetime(2024, 10, 13)
training_plan = create_training_plan(race_date, start_date)

for week in training_plan:
    print(f"Week {week['week']}:")
    for day in week['days']:
        print(f"  {day['date']}: {day['workout']}")