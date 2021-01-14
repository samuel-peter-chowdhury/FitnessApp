from app import db
from app.models import User, Routine, Exercise, ExerciseRoutineJoin
from app.services import UserService, RoutineService, ExerciseService, TableService

if __name__ == '__main__':
	print(ExerciseService.getAllExercises())