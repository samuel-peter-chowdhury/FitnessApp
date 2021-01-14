from app import db

class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(64), index=True, unique=True)
    email = db.Column(db.String(120), index=True, unique=True)
    password_hash = db.Column(db.String(128))
    routines = db.relationship('Routine', back_populates='user')

    def __repr__(self):
        return '<User {}>'.format(self.username)

class Routine(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(64))
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'))
    user = db.relationship('User', back_populates='routines')
    exercise_routine_joins = db.relationship('ExerciseRoutineJoin', back_populates='routine')

    def getExercises(self):
        return [x.exercise for x in self.exercise_routine_joins]

    def __repr__(self):
        return '<Routine {}{}>'.format(self.name, ','.join([str(x) for x in self.exercise_routine_joins]))

class ExerciseRoutineJoin(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    routine_id = db.Column(db.Integer, db.ForeignKey('routine.id'))
    routine = db.relationship('Routine', back_populates='exercise_routine_joins')
    exercise_id = db.Column(db.Integer, db.ForeignKey('exercise.id'))
    exercise = db.relationship('Exercise', back_populates='exercise_routine_joins')

    def __repr__(self):
        return '<ExerciseRoutineJoin {}>'.format(self.exercise)

class Exercise(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    ace_id = db.Column(db.Integer)
    name = db.Column(db.String(64))
    muscle = db.Column(db.String(64))
    equipment = db.Column(db.String(64))
    difficulty = db.Column(db.String(64))
    instructions = db.Column(db.Text)
    exercise_routine_joins = db.relationship('ExerciseRoutineJoin', back_populates='exercise')

    def getRoutines(self):
        return [x.routine for x in self.exercise_routine_joins]

    def __repr__(self):
        return '<Exercise {}>'.format(self.name)