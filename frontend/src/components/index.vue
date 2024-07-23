<template>
    <div class="abc container-fluid">
        <link rel="stylesheet" href="https://cdn.jsdelivr.net/npm/bootstrap@5.3.3/dist/css/bootstrap.min.css">
        <link rel="stylesheet" href="https://cdnjs.cloudflare.com/ajax/libs/font-awesome/6.1.1/css/all.min.css">
        <h1>AstralIDE - <span>Your Ultimate Coding Companion</span></h1>
        <div v-if="isSignup" class="row align-items-center g-lg-4 py-5">
            <div class="col-lg-7 text-center text-lg-start">
              
              <div class="container">
                <div class="header">Welcome to AstralIDE - Your Ultimate Coding Companion!</div>
                <div class="description">
                    AstralIDE is a modern code editor crafted for developers who value both functionality and ease of use. It provides an intuitive interface with essential tools for coding, including advanced syntax highlighting, intelligent code completion, and integrated debugging. Tailored for productivity, AstralIDE helps streamline your development process and enhance your coding efficiency.
                </div>
                <div class="features">
                    <div class="feature">
                        <h5>Frontend Excellence</h5>
                        <p>Built with Vue.js, AstralIDE offers a dynamic and responsive interface, ensuring a smooth user experience.</p>
                    </div>
                    <div class="feature">
                        <h5>Backend Brilliance</h5>
                        <p>Powered by Flask, our backend architecture guarantees fast and reliable performance.</p>
                    </div>
                    <div class="feature">
                        <h5>Effortless Communication</h5>
                        <p>With Axios handling frontend-backend communication, you get real-time updates and seamless data flow.</p>
                    </div>
                    <div class="feature">
                        <h5>Sleek Design</h5>
                        <p>Styled with Bootstrap, HTML, and CSS, AstralIDE provides a clean, modern look that’s easy on the eyes and intuitive to navigate.</p>
                    </div>
                </div>
                <div class="footer">
                    Join the AstralIDE community today and elevate your coding experience to new heights. Code faster, smarter, and more efficiently with AstralIDE!
                    <div class="contact">
                        <a href="mailto:contact@astralide.com" class="email">anirudhpabbaraju1103@gmail.com</a>
                        <a href="https://www.instagram.com/astralide" target="_blank" class="social-icon">
                          <i class="fab fa-instagram"></i>
                        </a>
                        <a href="https://www.linkedin.com/company/astralide" target="_blank" class="social-icon">
                          <i class="fab fa-linkedin"></i>
                        </a>
                    </div>
                </div>
            </div>
            </div>
            <div class="col-md-10 mx-auto col-lg-4">
                <p class="white2">SignUp Form</p>
                <form class="p-4 p-md-5 border rounded-3 bg-body-dark form-custom" @submit.prevent="validateForm">
                    <div class="form-floating mb-3 blue">
                        <input type="email" v-model="email" class="form-control" id="floatingInput" placeholder="name@example.com">
                        <label for="floatingInput" class="blue">Email address</label>
                        <div v-if="errors.email" class="text-danger">{{ errors.email }}</div>
                    </div>
                    <div class="form-floating mb-3 blue">
                        <input type="password" v-model="password" class="form-control" id="floatingPassword" placeholder="Password" @input="checkPasswordStrength">
                       
                        <label for="floatingPassword" class="blue">Password</label>
                        <i :class="passwordFieldIcon" @click="togglePasswordVisibility" class="position-absolute top-50 end-0 translate-middle-y pe-3" style="cursor: pointer;"></i>
                        <div v-if="errors.password" class="text-danger">{{ errors.password }}</div>
                        <small class="white">Strength: {{ passwordStrength }}</small>
                    </div>
                    <div class="form-floating mb-3 blue">
                        <input type="password" v-model="confirmPassword" class="form-control" id="floatingConfirmPassword" placeholder="Confirm Password">
                        <label for="floatingConfirmPassword" class="blue">Confirm Password</label>
                        <i :class="passwordFieldIcon" @click="togglePasswordVisibility" class="position-absolute top-50 end-0 translate-middle-y pe-3" style="cursor: pointer;"></i>
                        <div v-if="errors.confirmPassword" class="text-danger">{{ errors.confirmPassword }}</div>
                    </div>
                    <div class="checkbox mb-3">
                        <label class="white">
                            <input type="checkbox" v-model="rememberMe"> Remember me
                        </label>
                    </div>
                    <button class="w-100 btn btn-lg btn-primary" type="submit">Sign up</button>
                    <hr class="my-4">
                    <small class="white">By clicking Sign up, you agree to the terms of use.</small>
                    
                </form>
                <p class="white">Already Have an Account? <button class="btn btn-secondary" @click="toggle">Sign In</button></p>
              </div>
        </div>
        <div v-if="isSignin" class="row align-items-center g-lg-4 py-5">
            <div class="col-md-10 mx-auto col-lg-4">
                <p class="white2">SignIn Form</p>
                <form class="p-4 p-md-5 border rounded-3 bg-body-dark form-custom" @submit.prevent="validateForm">
                    <div class="form-floating mb-3 blue">
                        <input type="email" v-model="email" class="form-control" id="floatingInput" placeholder="name@example.com">
                        <label for="floatingInput" class="blue">Email address</label>
                        <div v-if="errors.email" class="text-danger">{{ errors.email }}</div>
                    </div>
                    <div class="form-floating mb-3 blue">
                        <input type="password" v-model="password" class="form-control" id="floatingPassword" placeholder="Password" @input="checkPasswordStrength">
                        <label for="floatingPassword" class="blue">Password</label>
                        <i :class="passwordFieldIcon" @click="togglePasswordVisibility" class="position-absolute top-50 end-0 translate-middle-y pe-3" style="cursor: pointer;"></i>
                        <div v-if="errors.password" class="text-danger">{{ errors.password }}</div>
                    </div>
                    <div class="checkbox mb-3">
                        <label class="white">
                            <input type="checkbox" v-model="rememberMe"> Remember me
                        </label>
                    </div>
                    <button class="w-100 btn btn-lg btn-primary" type="submit">Sign In</button>
                    <hr class="my-4">
                    <small class="white">By clicking Sign In, you agree to the terms of use.</small>
                 
                </form>
                <p class="white">New Here? <button class="btn btn-secondary" @click="toggle">Sign Up</button></p>
              </div>
            <div class="col-lg-7 text-center text-lg-start">
              
              <div class="container">
                <div class="header">Welcome to AstralIDE - Your Ultimate Coding Companion!</div>
                <div class="description">
                    AstralIDE is a modern code editor crafted for developers who value both functionality and ease of use. It provides an intuitive interface with essential tools for coding, including advanced syntax highlighting, intelligent code completion, and integrated debugging. Tailored for productivity, AstralIDE helps streamline your development process and enhance your coding efficiency.
                </div>
                <div class="features">
                    <div class="feature">
                        <h5>Frontend Excellence</h5>
                        <p>Built with Vue.js, AstralIDE offers a dynamic and responsive interface, ensuring a smooth user experience.</p>
                    </div>
                    <div class="feature">
                        <h5>Backend Brilliance</h5>
                        <p>Powered by Flask, our backend architecture guarantees fast and reliable performance.</p>
                    </div>
                    <div class="feature">
                        <h5>Effortless Communication</h5>
                        <p>With Axios handling frontend-backend communication, you get real-time updates and seamless data flow.</p>
                    </div>
                    <div class="feature">
                        <h5>Sleek Design</h5>
                        <p>Styled with Bootstrap, HTML, and CSS, AstralIDE provides a clean, modern look that’s easy on the eyes and intuitive to navigate.</p>
                    </div>
                </div>
                <div class="footer">
                    Join the AstralIDE community today and elevate your coding experience to new heights. Code faster, smarter, and more efficiently with AstralIDE!
                    <div class="contact">
                        <a href="mailto:contact@astralide.com" class="email">contact@astralide.com</a>
                        <a href="https://www.instagram.com/astralide" target="_blank" class="social-icon">
                          <i class="fab fa-instagram"></i>
                        </a>
                        <a href="https://www.linkedin.com/company/astralide" target="_blank" class="social-icon">
                          <i class="fab fa-linkedin"></i>
                        </a>
                    </div>
                </div>
            </div>
            </div>
            
        </div>

    </div>
</template>

<script>
    import axios from 'axios'
    import { useRouter } from 'vue-router';
    export default {
        name:'index',
        data(){
            return{
                isSignup:!true,
                isSignin:!false,
                email: '',
                password: '',
                confirmPassword: '',
                rememberMe: false,
                errors: {},
                passwordStrength: ''
            }
        },
        setup(){
            const router=useRouter();
            return {router};
        },
        methods:{
            toggle(){
                this.isSignup=!this.isSignup;
                this.isSignin=!this.isSignin;
            },
            checkPasswordStrength() {
                const strength = this.calculatePasswordStrength(this.password);
                this.passwordStrength = strength;
            },
            calculatePasswordStrength(password) {
                let strength = '';
                if (password.length < 6) {
                    strength = 'Weak';
                } else if (password.length >= 6 && password.length < 10) {
                    strength = 'Moderate';
                } else {
                    strength = 'Strong';
                }
                return strength;
            },
            togglePasswordVisibility() {
            },
            validateForm() {
                this.errors = {};
                if (!this.email) {
                    this.errors.email = 'Email is required';
                }
                if (!this.password) {
                    this.errors.password = 'Password is required';
                }
                if(this.isSignin){
                    this.loginform();
                } 
                else{
                if (this.password !== this.confirmPassword) {
                    this.errors.confirmPassword = 'Passwords do not match';
                }
                if (Object.keys(this.errors).length === 0) {
                  
                    if(this.passwordStrength!='Strong'){
                      this.errors.password='Password is not Strong re-enter'
                      this.password="";
                      this.confirmPassword="";
                    }
                    else{
                        this.registerform();
                    }
                }}
            },
            async registerform(){
                const response=await axios.post("http://127.0.0.1:5000/api/user_register",
                    JSON.stringify({
                        'email':this.email,
                        'password':this.password
                    }),
                    {
                        headers:{
                            'Content-Type':'application/json'
                        }
                    }
                );

                if(response.status===200){
                    alert('Registered Successfully and You are automatically Moved to Page!');
                    this.isSignin=true;
                    this.isSignup=false;
                }
                else{
                    alert('Oops iguess You are registered already try SignIn!');
                }
            },
            async loginform(){
                const response=await axios.post("http://127.0.0.1:5000/api/user_login",
                    JSON.stringify({
                        'email':this.email,
                        'password':this.password
                    }),
                    {
                        headers:{
                            'Content-Type':'application/json'
                        }
                    }
                );

                if(response.status===200){
                    alert('Logged In Successfully');
                    const access_token=response.data.access_token;
                    const info={
                        "email":response.data.info["email"],
                        "id":response.data.info["id"],
                    };
                    localStorage.setItem("access_token",access_token);
                    localStorage.setItem("info",JSON.stringify(info));
                    localStorage.setItem("lan","welcome");
                    this.$router.push("/editor_page");
                }
                else{
                    alert("Oops ig You haven'\t even registered already try SignUP!");
                }
            }
        },

    }
</script>

<style scoped>
   .abc{
     background-color: #0f172a;
     min-height:100vh;
     display: flex;
     flex-direction: column;
     justify-content: space-between;
     align-items: center;
   }
   h1{
    color:#06b6d4;
    font-weight: bold;
    font-size:40px;
   }
   span{
    color:lightpink;
   }
   body {
    font-family: 'Arial', sans-serif;
    background-color: #f8f9fa;
    color: #333;
    margin: 0;
    padding: 0;
    }
    .container {
        margin-top: 50px;
        text-align: center;
    }
    .header {
        font-size: 2.5em;
        margin-bottom: 20px;
        color: #0ea5e9;
    }
    .description {
        font-size: 1.2em;
        margin-bottom: 40px;
        color:#fcd34d;
    }
    .features {
        text-align: left;
        margin: auto;
        max-width: 800px;
        color:#4ade80;
    }
    .feature {
        margin-bottom: 20px;
    }
    .footer {
        margin-top: 40px;
        font-size: 0.9em;
        color: #eff6ff;
    }
    .x{
        background-color:#a855f7;
    }
    h5{
        color:#f7fee7;
    }
    .form-custom {
        background-color: #020617;
        padding: 2rem;
        border-radius: 1rem;
        box-shadow: 0 4px 8px rgba(0, 0, 0, 0.1);
      }
      .form-control {
        border-radius: 0.5rem;
        margin-bottom: 1rem;
      }
      .form-control:focus {
        border-color: #6366f1;
        box-shadow: 0 0 0 0.2rem rgba(99, 102, 241, 0.25);
      }
      .btn-primary {
        background-color: #6366f1;
        border-color: #6366f1;
      }
      .btn-primary:hover {
        background-color: #4f46e5;
        border-color: #4f46e5;
      }
      .btn-secondary {
        background-color: #10b981;
        border-color: #10b981;
      }
      .btn-secondary:hover {
        background-color: #059669;
        border-color: #059669;
      }
    .white{
        color:#e2e8f0;
        text-align:center;
    }
    .blue{
        color:#06b6d4;
        font-weight:bold;
    }
    .contact {
        margin-top: 20px;
      }
      .contact .email {
        display: block;
        color: #06b6d4;
        text-decoration: none;
        margin-bottom: 10px;
      }
      .contact .social-icon {
        color: #06b6d4;
        margin-right: 10px;
        font-size: 1.5em;
      }
      .contact .social-icon:hover {
        color: #4f46e5;
      }
      .white2{
        color:#22c55e;
        font-weight: bold;
        text-align: center;
        font-size:large;
      }
</style>