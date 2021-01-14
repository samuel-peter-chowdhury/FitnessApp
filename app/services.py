from app import db
from app.models import User, Routine, Exercise, ExerciseRoutineJoin

def commit(entity):
	db.session.add(entity)
	db.session.commit()

class Initializer:
	@staticmethod
	def initialize():
		print("...Initializing database...")
		if (len(ExerciseService.getAllExercises()) <= 0):
			print("...Initializing Exercises...")
		print("...Initialization complete...")

class UserService:
	@staticmethod
	def addUser(username, email, password_hash=None):
		commit(User(username=username, email=email, password_hash=password_hash))

	@staticmethod
	def getAllUsers():
		return db.session.query(User).all()

	@staticmethod
	def getUserById(id):
		return db.session.query(User).get(id)

	@staticmethod
	def getUserByUsername(username):
		return db.session.query(User).filter(User.username == username).all()[0]

	@staticmethod
	def getUserByEmail(email):
		return db.session.query(User).filter(User.email == email).all()[0]

class RoutineService:
	@staticmethod
	def addRoutine(name, user_id):
		commit(Routine(name=name, user_id=user_id))

	@staticmethod
	def getAllRoutines():
		return db.session.query(Routine).all()

	@staticmethod
	def getRoutineById(id):
		return db.session.query(Routine).get(id)

	@staticmethod
	def getRoutinesByUserId(user_id):
		return db.session.query(Routine).filter(Routine.user_id == user_id).all()

class ExerciseService:
	@staticmethod
	def addExercise(ace_id, name, muscle, equipment, difficulty, instructions):
		commit(Exercise(ace_id=ace_id, name=name, muscle=muscle, equipment=equipment, difficulty=difficulty, instructions=instructions))

	@staticmethod
	def getAllExercises():
		return db.session.query(Exercise).all()

	@staticmethod
	def getExerciseById(id):
		return db.session.query(Exercise).get(id)

	@staticmethod
	def getExerciseByAceId(ace_id):
		return db.session.query(Exercise).filter(Exercise.ace_id == ace_id).all()[0]

	@staticmethod
	def getExerciseByName(name):
		return db.session.query(Exercise).filter(Exercise.name == name).all()[0]

	@staticmethod
	def getExercisesByMuscle(muscle):
		return db.session.query(Exercise).filter(Exercise.muscle == muscle).all()

	@staticmethod
	def getExercisesByEquipment(equipment):
		return db.session.query(Exercise).filter(Exercise.equipment == equipment).all()

	@staticmethod
	def getExercisesByDifficulty(difficulty):
		return db.session.query(Exercise).filter(Exercise.difficulty == difficulty).all()