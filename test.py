from app import db
from app.models import User, Routine, Exercise, ExerciseRoutineJoin
from app.services import UserService, RoutineService

if __name__ == '__main__':
	print(UserService.getUserByUsername('john').routines[0].getExercises())