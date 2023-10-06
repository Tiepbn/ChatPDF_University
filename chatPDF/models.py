from chatPDF import db

class User(db.Model, UserMixin):
    id = db.Column(db.Integer(), primary_key=True)
    username = db.Column(db.String(length=30), nullable=False, unique=True)
    email_address = db.Column(db.String(length=50), nullable=False, unique=True)
    password_hash = db.Column(db.String(length=60), nullable=False, unique=True)
    # budget = db.Column(db.Integer(), nullable=False, default=1000)
    # # owned_user là mã đơn, và lazy = lấy hết tất cả những vật thể của vật phẩm
    # items = db.relationship('Item', backref='owned', lazy = True)

    @property
    def password(self):
        return self.password
    
    @password.setter
    def password(self, plain_text_password):
        # tao ham bam cho mk 
        self.password_hash = bcrypt.generate_password_hash(plain_text_password).decode('utf-8')
    def check_password_correction(self, attempted_password):
        return bcrypt.check_password_hash(self.password_hash, attempted_password)
