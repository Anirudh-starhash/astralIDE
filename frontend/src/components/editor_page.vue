<template>
  <div class="abc">
    <code_header class="full-width-header" />
    <div class="container-fluid">
      <explorer v-if="explorer" :choosen="value"/>
      <div class="center">
         <h1>Astrall<span>IDE</span></h1>
         <div class="editor-wrapper">
            <div class="menu-bar">
             <a @click="downloadCode" class="menu-button">
               <svg xmlns="http://www.w3.org/2000/svg" width="16" height="16" fill="currentColor" class="bi bi-cloud-arrow-down green" viewBox="0 0 16 16">
                 <path fill-rule="evenodd" d="M7.646 10.854a.5.5 0 0 0 .708 0l2-2a.5.5 0 0 0-.708-.708L8.5 9.293V5.5a.5.5 0 0 0-1 0v3.793L6.354 8.146a.5.5 0 1 0-.708.708z"/>
                 <path d="M4.406 3.342A5.53 5.53 0 0 1 8 2c2.69 0 4.923 2 5.166 4.579C14.758 6.804 16 8.137 16 9.773 16 11.569 14.502 13 12.687 13H3.781C1.708 13 0 11.366 0 9.318c0-1.763 1.266-3.223 2.942-3.593.143-.863.698-1.723 1.464-2.383m.653.757c-.757.653-1.153 1.44-1.153 2.056v.448l-.445.049C2.064 6.805 1 7.952 1 9.318 1 10.785 2.23 12 3.781 12h8.906C13.98 12 15 10.988 15 9.773c0-1.216-1.02-2.228-2.313-2.228h-.5v-.5C12.188 4.825 10.328 3 8 3a4.53 4.53 0 0 0-2.941 1.1z"/>
               </svg>
               <p class="white">Download</p>
             </a>
              <a @click="renameFile" class="menu-button">
                <svg xmlns="http://www.w3.org/2000/svg" width="16" height="16" fill="currentColor" class="bi bi-pencil-square yellow" viewBox="0 0 16 16">
                  <path d="M15.502 1.94a.5.5 0 0 1 0 .706L14.459 3.69l-2-2L13.502.646a.5.5 0 0 1 .707 0l1.293 1.293zm-1.75 2.456-2-2L4.939 9.21a.5.5 0 0 0-.121.196l-.805 2.414a.25.25 0 0 0 .316.316l2.414-.805a.5.5 0 0 0 .196-.12l6.813-6.814z"/>
                  <path fill-rule="evenodd" d="M1 13.5A1.5 1.5 0 0 0 2.5 15h11a1.5 1.5 0 0 0 1.5-1.5v-6a.5.5 0 0 0-1 0v6a.5.5 0 0 1-.5.5h-11a.5.5 0 0 1-.5-.5v-11a.5.5 0 0 1 .5-.5H9a.5.5 0 0 0 0-1H2.5A1.5 1.5 0 0 0 1 2.5z"/>
                </svg>
                <p class="white">Rename</p>
              </a>
              <a @click="runCode" class="menu-button">
                <svg xmlns="http://www.w3.org/2000/svg" width="16" height="16" fill="currentColor" class="bi bi-caret-right-fill red" viewBox="0 0 16 16">
                  <path d="m12.14 8.753-5.482 4.796c-.646.566-1.658.106-1.658-.753V3.204a1 1 0 0 1 1.659-.753l5.48 4.796a1 1 0 0 1 0 1.506z"/>
                </svg>
                <p class="white" >Run</p>
              </a>
              <a @click="saveCode" class="menu-button">
                <svg xmlns="http://www.w3.org/2000/svg" fill="aliceblue" xmlns:xlink="http://www.w3.org/1999/xlink" version="1.1" id="Icons" viewBox="0 0 32 32" xml:space="preserve" class="aliceblue">
                  <path d="M14,23c0-5.5,4.5-10,10-10c1.2,0,2.3,0.2,3.3,0.6l2.9-4.4c0.4-0.6,0.6-1.2,0.7-1.9C31,7.2,31,7.1,31,7c0-0.1,0-0.1,0-0.2  c0-0.8-0.1-1.5-0.4-2.3c-0.7-1.4-2-2.4-3.5-2.6c-0.2,0-0.4,0-0.6,0c-0.1,0-0.1,0-0.2,0c-0.1,0-0.2,0-0.3,0c0,0,0,0,0,0c0,0,0,0,0,0  H9.5C9.4,2,9.3,2,9.2,2.1C9.2,2,9.1,2,9,2C6.2,2,4,4.2,4,7c0,0.7,0.2,1.3,0.6,1.9C5.4,10.2,6.8,11,8.4,11h1.2L1.8,22.8  c-0.9,1.4-1,3.1-0.3,4.6c0.7,1.4,2,2.4,3.5,2.6c0.2,0,0.4,0,0.6,0h11.4C15.1,28.2,14,25.7,14,23z M8.4,9C7.5,9,6.7,8.6,6.3,7.9  C6.1,7.6,6,7.3,6,7c0-1.7,1.3-3,3-3c0.1,0,0.2,0,0.2-0.1C9.3,4,9.4,4,9.5,4h12.7c-1.7,2.2-1,4.2-0.6,5c0,0,0,0,0,0H8.4z"/>
                  <path d="M25,15.1v8.5l1.3-1.3c0.4-0.4,1-0.4,1.4,0s0.4,1,0,1.4l-3,3c-0.1,0.1-0.2,0.2-0.3,0.2C24.3,27,24.1,27,24,27s-0.3,0-0.4-0.1  c-0.1-0.1-0.2-0.1-0.3-0.2l-3-3c-0.4-0.4-0.4-1,0-1.4s1-0.4,1.4,0l1.3,1.3v-8.5c-3.9,0.5-7,3.9-7,7.9c0,4.4,3.6,8,8,8s8-3.6,8-8  C32,18.9,28.9,15.6,25,15.1z"/>
                </svg>
                <p class="white" >Save</p>
              </a>
              <select v-model="selectedLanguage" @change="updateCode" class="language-select">
                <option value="welcome">Welcome</option>
                <option value="cpp">C++</option>
                <option value="py">Python</option>
                <option value="java">Java</option>
                <option value="c">C</option>
                <option value="kt">Kotlin</option>
                <option value="js">JavaScript</option>
                <option value="html">Html</option>
                <option value="R">R</option>
                <option value="php">PHP</option>
                <option value="cs">C#</option>
                <option value="ml">OCaml</option>
                <option value="vb">VB</option>
                <option value="rb">Ruby</option>
                <option value="pl">Perl</option>
                <option value="pas">Pascal</option>
                <option value="cob">Cobol</option>
                <option value="f95">Fortran</option>
                <option value="hs">Haskell</option>
                <option value="S">Assembly</option>
                <option value="m">Objective(C)</option>
                <option value="sql">Sqlite</option>
                <option value="swift">Swift</option>
                <option value="rs">Rust</option>
                <option value="go">Go</option>
                <option value="bash">Bash</option>
              </select>


              <a @click="beautifyCode" class="menu-button">
                <svg xmlns="http://www.w3.org/2000/svg" fill="aqua" width="16" height="16" viewBox="0 0 24 24" class="aqua">
                  <path d="M9 22h1v-2h-.989C8.703 19.994 6 19.827 6 16c0-1.993-.665-3.246-1.502-4C5.335 11.246 6 9.993 6 8c0-3.827 2.703-3.994 3-4h1V2H8.998C7.269 2.004 4 3.264 4 8c0 2.8-1.678 2.99-2.014 3L2 13c.082 0 2 .034 2 3 0 4.736 3.269 5.996 5 6zm13-11c-.082 0-2-.034-2-3 0-4.736-3.269-5.996-5-6h-1v2h.989c.308.006 3.011.173 3.011 4 0 1.993.665 3.246 1.502 4-.837.754-1.502 2.007-1.502 4 0 3.827-2.703 3.994-3 4h-1v2h1.002C16.731 21.996 20 20.736 20 16c0-2.8 1.678-2.99 2.014-3L22 11z"/>
                </svg>
                <p class="white">Beautify</p>
              </a>

              <a v-if="selectedLanguage!=`welcome`" class="menu-button">
                <svg xmlns="http://www.w3.org/2000/svg"  fill="currentColor" class="bi bi-file-earmark-text aqua" viewBox="0 0 16 16">
                  <path d="M5.5 7a.5.5 0 0 0 0 1h5a.5.5 0 0 0 0-1zM5 9.5a.5.5 0 0 1 .5-.5h5a.5.5 0 0 1 0 1h-5a.5.5 0 0 1-.5-.5m0 2a.5.5 0 0 1 .5-.5h2a.5.5 0 0 1 0 1h-2a.5.5 0 0 1-.5-.5"/>
                  <path d="M9.5 0H4a2 2 0 0 0-2 2v12a2 2 0 0 0 2 2h8a2 2 0 0 0 2-2V4.5zm0 1v2A1.5 1.5 0 0 0 11 4.5h2V14a1 1 0 0 1-1 1H4a1 1 0 0 1-1-1V2a1 1 0 0 1 1-1z"/>
                </svg>
                <p  class="file-name white">File: {{ fileName }}</p>
              </a>

            </div>
          <textarea v-model="code" rows="20" cols="80" class="code-textarea" spellcheck="false"></textarea><br>
        </div>
        <pre style="background-color:#020617; color:white;">Status -> {{ msg }}</pre>
        <pre  style="background-color:#020617; color:white;">Output -> {{ output }}</pre>
      </div>
      <terminal v-if="terminal"/>
      
    </div>
    <footer_page class="full-width-header" />
  </div>
</template>

<script>
import axios from 'axios';
import code_header from './code_header.vue';
import footer_page from './footer.vue';
import explorer from './explorer.vue'
import terminal from './terminal.vue'
import { useRouter } from 'vue-router';

export default {
  name:'editor_page',
  data() {
    return {
      code: '',
      output: '',
      msg: '',
      isLoading: false,
      selectedLanguage: 'welcome',
      fileName: '',
      terminal:false,
      explorer:true,
    };
  },
  setup(){
    const router=useRouter();
    return {router};
  },
  async mounted(){
    const access_token=localStorage.getItem("access_token")
        if(!access_token){
          alert('You need to login first to come here!')
          this.$router.push("/");
        }
        else{
          this.id=JSON.parse(localStorage.getItem("info")).id;
          try{
            const r=await axios.post("http://127.0.0.1:5000/api/user_check_permission",null,
              {
                headers:{
                  Authorization:`Bearer ${access_token}`
                }
              }
            );
            if(r.status===200){
              this.selectedLanguage=localStorage.getItem("lan");
              this.updateCode();
              
            }
            else{
              localStorage.removeItem("access_token")
              localStorage.removeItem("info")
              this.$router.push("/unauthorized");
            }
          }
          catch(error){
            console.log(error);
          }
        }
  },
  methods: {
    async runCode() {
      this.isLoading = true;
      this.msg = 'Running...';
      this.output = '';
      try {
        if(this.selectedLanguage==="cpp"){
          const response = await axios.post('http://127.0.0.1:5000/api/runCPP',
            JSON.stringify({ code: this.code, language: this.selectedLanguage }), {
              headers: { 'Content-Type': 'application/json' }
            }
          );

          if (response.status === 200) {
            this.msg = response.data.msg || 'Code ran successfully.';
            this.output = response.data.output;
          } else {
            this.msg = 'Error: ' + response.data.msg;
            this.output = response.data.error || 'An error occurred.';
          }

        }
        else if(this.selectedLanguage==="Java"){
          const response = await axios.post('http://127.0.0.1:5000/api/runJAVA',
            JSON.stringify({ code: this.code, language: this.selectedLanguage }), {
              headers: { 'Content-Type': 'application/json' }
            }
          );

          if (response.status === 200) {
            this.msg = response.data.msg || 'Code ran successfully.';
            this.output = response.data.output;
          } else {
            this.msg = 'Error: ' + response.data.msg;
            this.output = response.data.error || 'An error occurred.';
          }

        }
        else if(this.selectedLanguage==="C"){
          const response = await axios.post('http://127.0.0.1:5000/api/runC',
            JSON.stringify({ code: this.code, language: this.selectedLanguage }), {
              headers: { 'Content-Type': 'application/json' }
            }
          );

          if (response.status === 200) {
            this.msg = response.data.msg || 'Code ran successfully.';
            this.output = response.data.output;
          } else {
            this.msg = 'Error: ' + response.data.msg;
            this.output = response.data.error || 'An error occurred.';
          }

        }
        else if(this.selectedLanguage==="js"){
          const response = await axios.post('http://127.0.0.1:5000/api/runJS',
            JSON.stringify({ code: this.code, language: this.selectedLanguage }), {
              headers: { 'Content-Type': 'application/json' }
            }
          );

          if (response.status === 200) {
            this.msg = response.data.msg || 'Code ran successfully.';
            this.output = response.data.output;
          } else {
            this.msg = 'Error: ' + response.data.msg;
            this.output = response.data.error || 'An error occurred.';
          }

        }
        else if(this.selectedLanguage==="kt"){
          const response = await axios.post('http://127.0.0.1:5000/api/runKotlin',
            JSON.stringify({ code: this.code, language: this.selectedLanguage }), {
              headers: { 'Content-Type': 'application/json' }
            }
          );

          if (response.status === 200) {
            this.msg = response.data.msg || 'Code ran successfully.';
            this.output = response.data.output;
          } else {
            this.msg = 'Error: ' + response.data.msg;
            this.output = response.data.error || 'An error occurred.';
          }

        }
        else if(this.selectedLanguage==="R"){
          const response = await axios.post('http://127.0.0.1:5000/api/runR',
            JSON.stringify({ code: this.code, language: this.selectedLanguage }), {
              headers: { 'Content-Type': 'application/json' }
            }
          );

          if (response.status === 200) {
            this.msg = response.data.msg || 'Code ran successfully.';
            this.output = response.data.output;
          } else {
            this.msg = 'Error: ' + response.data.msg;
            this.output = response.data.error || 'An error occurred.';
          }

        }
        else if(this.selectedLanguage==="py"){
          const response = await axios.post('http://127.0.0.1:5000/api/runPython',
            JSON.stringify({ code: this.code, language: this.selectedLanguage }), {
              headers: { 'Content-Type': 'application/json' }
            }
          );

          if (response.status === 200) {
            this.msg = response.data.msg || 'Code ran successfully.';
            this.output = response.data.output;
          } else {
            this.msg = 'Error: ' + response.data.msg;
            this.output = response.data.error || 'An error occurred.';
          }

        }
        else if(this.selectedLanguage==="go"){
          const response = await axios.post('http://127.0.0.1:5000/api/runGo',
            JSON.stringify({ code: this.code, language: this.selectedLanguage }), {
              headers: { 'Content-Type': 'application/json' }
            }
          );

          if (response.status === 200) {
            this.msg = response.data.msg || 'Code ran successfully.';
            this.output = response.data.output;
          } else {
            this.msg = 'Error: ' + response.data.msg;
            this.output = response.data.error || 'An error occurred.';
          }

        }
        else if(this.selectedLanguage==="bash"){
          const response = await axios.post('http://127.0.0.1:5000/api/runBash',
            JSON.stringify({ code: this.code, language: this.selectedLanguage }), {
              headers: { 'Content-Type': 'application/json' }
            }
          );

          if (response.status === 200) {
            this.msg = response.data.msg || 'Code ran successfully.';
            this.output = response.data.output;
          } else {
            this.msg = 'Error: ' + response.data.msg;
            this.output = response.data.error || 'An error occurred.';
          }

        }
        else if(this.selectedLanguage==="rs"){
          const response = await axios.post('http://127.0.0.1:5000/api/runRust',
            JSON.stringify({ code: this.code, language: this.selectedLanguage }), {
              headers: { 'Content-Type': 'application/json' }
            }
          );

          if (response.status === 200) {
            this.msg = response.data.msg || 'Code ran successfully.';
            this.output = response.data.output;
          } else {
            this.msg = 'Error: ' + response.data.msg;
            this.output = response.data.error || 'An error occurred.';
          }

        }
        else if(this.selectedLanguage==="swift"){
          const response = await axios.post('http://127.0.0.1:5000/api/runSwift',
            JSON.stringify({ code: this.code, language: this.selectedLanguage }), {
              headers: { 'Content-Type': 'application/json' }
            }
          );

          if (response.status === 200) {
            this.msg = response.data.msg || 'Code ran successfully.';
            this.output = response.data.output;
          } else {
            this.msg = 'Error: ' + response.data.msg;
            this.output = response.data.error || 'An error occurred.';
          }

        }
        else if(this.selectedLanguage==="sql"){
          const response = await axios.post('http://127.0.0.1:5000/api/runSqlite',
            JSON.stringify({ code: this.code, language: this.selectedLanguage }), {
              headers: { 'Content-Type': 'application/json' }
            }
          );

          if (response.status === 200) {
            this.msg = response.data.msg || 'Code ran successfully.';
            this.output = response.data.output;
          } else {
            this.msg = 'Error: ' + response.data.msg;
            this.output = response.data.error || 'An error occurred.';
          }

        }
        else if(this.selectedLanguage==="pl"){
          const response = await axios.post('http://127.0.0.1:5000/api/runPerl',
            JSON.stringify({ code: this.code, language: this.selectedLanguage }), {
              headers: { 'Content-Type': 'application/json' }
            }
          );

          if (response.status === 200) {
            this.msg = response.data.msg || 'Code ran successfully.';
            this.output = response.data.output;
          } else {
            this.msg = 'Error: ' + response.data.msg;
            this.output = response.data.error || 'An error occurred.';
          }

        }
        else if(this.selectedLanguage==="rb"){
          const response = await axios.post('http://127.0.0.1:5000/api/runRuby',
            JSON.stringify({ code: this.code, language: this.selectedLanguage }), {
              headers: { 'Content-Type': 'application/json' }
            }
          );

          if (response.status === 200) {
            this.msg = response.data.msg || 'Code ran successfully.';
            this.output = response.data.output;
          } else {
            this.msg = 'Error: ' + response.data.msg;
            this.output = response.data.error || 'An error occurred.';
          }

        }
        else if(this.selectedLanguage==="S"){
          const response = await axios.post('http://127.0.0.1:5000/api/runAssembly',
            JSON.stringify({ code: this.code, language: this.selectedLanguage }), {
              headers: { 'Content-Type': 'application/json' }
            }
          );

          if (response.status === 200) {
            this.msg = response.data.msg || 'Code ran successfully.';
            this.output = response.data.output;
          } else {
            this.msg = 'Error: ' + response.data.msg;
            this.output = response.data.error || 'An error occurred.';
          }

        }
        else if(this.selectedLanguage==="m"){
          const response = await axios.post('http://127.0.0.1:5000/api/runObjectiveC',
            JSON.stringify({ code: this.code, language: this.selectedLanguage }), {
              headers: { 'Content-Type': 'application/json' }
            }
          );

          if (response.status === 200) {
            this.msg = response.data.msg || 'Code ran successfully.';
            this.output = response.data.output;
          } else {
            this.msg = 'Error: ' + response.data.msg;
            this.output = response.data.error || 'An error occurred.';
          }

        }
        else if(this.selectedLanguage==="ml"){
          const response = await axios.post('http://127.0.0.1:5000/api/runOCaml',
            JSON.stringify({ code: this.code, language: this.selectedLanguage }), {
              headers: { 'Content-Type': 'application/json' }
            }
          );

          if (response.status === 200) {
            this.msg = response.data.msg || 'Code ran successfully.';
            this.output = response.data.output;
          } else {
            this.msg = 'Error: ' + response.data.msg;
            this.output = response.data.error || 'An error occurred.';
          }

        }
        else if(this.selectedLanguage==="cs"){
          const response = await axios.post('http://127.0.0.1:5000/api/runC#',
            JSON.stringify({ code: this.code, language: this.selectedLanguage }), {
              headers: { 'Content-Type': 'application/json' }
            }
          );

          if (response.status === 200) {
            this.msg = response.data.msg || 'Code ran successfully.';
            this.output = response.data.output;
          } else {
            this.msg = 'Error: ' + response.data.msg;
            this.output = response.data.error || 'An error occurred.';
          }

        }
        else if(this.selectedLanguage==="f95"){
          const response = await axios.post('http://127.0.0.1:5000/api/runFortran',
            JSON.stringify({ code: this.code, language: this.selectedLanguage }), {
              headers: { 'Content-Type': 'application/json' }
            }
          );

          if (response.status === 200) {
            this.msg = response.data.msg || 'Code ran successfully.';
            this.output = response.data.output;
          } else {
            this.msg = 'Error: ' + response.data.msg;
            this.output = response.data.error || 'An error occurred.';
          }

        }
        else if(this.selectedLanguage==="cob"){
          const response = await axios.post('http://127.0.0.1:5000/api/runCobol',
            JSON.stringify({ code: this.code, language: this.selectedLanguage }), {
              headers: { 'Content-Type': 'application/json' }
            }
          );

          if (response.status === 200) {
            this.msg = response.data.msg || 'Code ran successfully.';
            this.output = response.data.output;
          } else {
            this.msg = 'Error: ' + response.data.msg;
            this.output = response.data.error || 'An error occurred.';
          }

        }
        else if(this.selectedLanguage==="vb"){
          const response = await axios.post('http://127.0.0.1:5000/api/runVBModule',
            JSON.stringify({ code: this.code, language: this.selectedLanguage }), {
              headers: { 'Content-Type': 'application/json' }
            }
          );

          if (response.status === 200) {
            this.msg = response.data.msg || 'Code ran successfully.';
            this.output = response.data.output;
          } else {
            this.msg = 'Error: ' + response.data.msg;
            this.output = response.data.error || 'An error occurred.';
          }

        }
        else if(this.selectedLanguage==="hs"){
          const response = await axios.post('http://127.0.0.1:5000/api/runHaskell',
            JSON.stringify({ code: this.code, language: this.selectedLanguage }), {
              headers: { 'Content-Type': 'application/json' }
            }
          );

          if (response.status === 200) {
            this.msg = response.data.msg || 'Code ran successfully.';
            this.output = response.data.output;
          } else {
            this.msg = 'Error: ' + response.data.msg;
            this.output = response.data.error || 'An error occurred.';
          }

        }
        else if(this.selectedLanguage==="php"){
          const response = await axios.post('http://127.0.0.1:5000/api/runPHP',
            JSON.stringify({ code: this.code, language: this.selectedLanguage }), {
              headers: { 'Content-Type': 'application/json' }
            }
          );

          if (response.status === 200) {
            this.msg = response.data.msg || 'Code ran successfully.';
            this.output = response.data.output;
          } else {
            this.msg = 'Error: ' + response.data.msg;
            this.output = response.data.error || 'An error occurred.';
          }

        }
        else if(this.selectedLanguage==="pas"){
          const response = await axios.post('http://127.0.0.1:5000/api/runPascal',
            JSON.stringify({ code: this.code, language: this.selectedLanguage }), {
              headers: { 'Content-Type': 'application/json' }
            }
          );

          if (response.status === 200) {
            this.msg = response.data.msg || 'Code ran successfully.';
            this.output = response.data.output;
          } else {
            this.msg = 'Error: ' + response.data.msg;
            this.output = response.data.error || 'An error occurred.';
          }

        }
        else{
          this.msg='HTML code can\'t be compiled or interepretted'
          this.output='None!' 
        }
      
      
      } catch (error) {
        console.error('Error running code:', error);
        this.msg = 'Failed to run code.';
        this.output = error.message;
      } finally {
        this.isLoading = false;
      }
    },
    downloadCode() {
    let extension;
    switch (this.selectedLanguage) {
      case 'cpp':
        extension = 'cpp';
        break;
      case 'Java':
        extension = 'java';
        break;
      case 'py':
        extension = 'py';
        break;
      case 'C':
        extension = 'c';
        break;
      case 'js':
        extension = 'js';
        break;
      case 'Html':
        extension = 'html';
        break;
      case 'R':
        extension = 'r';
        break;
      case 'kt':
        extension = 'kt';
        break;
      case 'php':
        extension = 'php';
        break;
      case 'vb':
        extension = 'vb';
        break;
      case 'cs':
        extension = 'cs';
        break;
      case 'ml':
        extension = 'ml';
        break;
      case 'm':
        extension = 'm';
        break;
      case 'S':
        extension = 'S';
        break;
      case 'cob':
        extension = 'cob';
        break;
      case 'pas':
        extension = 'pas';
        break;
      case 'rb':
        extension = 'rb';
        break;
      case 'pl':
        extension = 'pl';
        break;
      case 'sql':
        extension = 'sql';
        break;
      case 'f95':
        extension = 'f95';
        break;
      case 'hs':
        extension = 'hs';
        break;
      case 'rs':
        extension = 'rs';
        break;
      case 'swift':
        extension = 'swift';
        break;
      case 'go':
        extension = 'go';
        break;
      case 'bash':
        extension = 'bash';
        break;
      default:
        extension = 'txt';
    }

    let fileName = this.fileName;
    if (!fileName.endsWith(`.${extension}`)) {
      fileName = `${fileName.split('.')[0]}.${extension}`;
    }

    const blob = new Blob([this.code], { type: 'text/plain' });
    const link = document.createElement('a');
    link.href = URL.createObjectURL(blob);
    link.download = fileName;
    link.click();
    URL.revokeObjectURL(link.href);
  },
    renameFile() {
      const newName = prompt('Enter new file name:', this.fileName);
      if (newName) {
        this.fileName = newName;
      }
    },
    beautifyCode() {
      // Implement beautify logic here
      alert('Beautify not implemented yet.');
    },
    updateCode() {
      const defaultCodes = {
        cpp: `#include<iostream>
using namespace std;
int main(){
  cout<<"Hello World";
}`,
        Java: `public class Main{
  public static void main(String args []){
    System.out.println("Hello World");
  }
}`,
          py: `print('Hello World')`,
          C: `#include<stdio.h>
void main(){
  printf("Hello world");
}`,
        js: `console.log("Hello World");`,
        Html: `<!DOCTYPE html>
<html lang="en">
  <head>
      <meta charset="UTF-8">
      <meta name="viewport" content="width=device-width, initial-scale=1.0">
      <title>Document</title>
  </head>
  <body>
                  
  </body>
</html>`,
        R: `print('Hello World')`,
        kt:`fun main() {
    println("Hello World")
}`,
      php:`<?php

echo "Hello World";`,
      cs:`using System;
class HelloWorld {
  static void Main() {
    Console.WriteLine("Hello World");
  }
}`,
      vb:`Module VBModule
    Sub Main()
        Console.WriteLine("Hello World")
    End Sub
End Module`,
      ml:`print_string "Hello world!"`,
      m:`#import <Foundation/Foundation.h>

int main (int argc, const char * argv[])
{
        NSAutoreleasePool *pool = [[NSAutoreleasePool alloc] init];
        NSLog (@"Hello World");
        [pool drain];
        return 0;
}`,
      S:`.data
.text
.global main
main:
  # your code goes here
  xor	%eax, %eax
  ret`,
      sql:`/* Enter your sql queries here */`,
      pl:`print "Hello World";`,
      rb:`puts "Hello World"`,
      cob:`  IDENTIFICATION DIVISION.
        PROGRAM-ID. hello.
        PROCEDURE DIVISION.
            DISPLAY "Hello World".
            STOP RUN.`,
      pas:`program Hello;
begin
  writeln ('Hello World')
end.`,
      f95:`Program Hello
Print *, "Hello World"
End Program Hello`,
      hs:`main = putStrLn "Hello World"`,
      go:`package main
import "fmt"

func main() {
    fmt.Println("Hello World")
}`,
      rs:`fn main() {
    println!("Hello World");
}`,
      bash:`echo "Hello World";`,
      swift:`print("Hello World")`
      
      };
      if(this.selectedLanguage=='welcome'){
        this.code=`                 AstralIDE

              Editing Evolved
              
              New Text File: Ctrl+N

              New File: Ctrl+Alt+Windows+N

              New Window: Ctrl+Shift+N

              Open File: Ctrl+O
              
              Open Folder: Ctrl+K Ctrl+O
              `

      }
      else{
        this.code = defaultCodes[this.selectedLanguage];
        localStorage.setItem("lan",this.selectedLanguage.toLowerCase())
        this.fileName="code."+this.selectedLanguage.toLowerCase()
      }
    
    },
  },
  components: {
    code_header,
    footer_page,
    explorer,
    terminal
  },
  computed:{
    value(){
      return localStorage.getItem("lan");
    }
  }
};
</script>

<style scoped>
  .abc {
    background-color: #0d1117; /* GitHub dark ColorBind(beta) background color */
    color: white; /* Text color for the entire page */
    min-height: 100vh; /* Ensure the page fills the viewport height */
    display: flex;
    flex-direction: column;
    align-items: center;
  }


  .full-width-header {
    width: 100%;
    height:10vh;
   /* Take full width of the parent container */
  }

  .container-fluid {
    display: flex;
    flex-direction: row;
    justify-content: space-around;
    min-height:100vh;
    width:100%;
    gap:10px;
  }


  h1 {
    text-align: center;
    color:#7dd3fc;
  }
  h2{
    color:cornflowerblue;
  }
  h3{
    color:gainsboro;
  }

  textarea, button {
    margin-bottom: 10px;
  }



  
  .center{
    display: flex;
    flex-direction: column;
    min-height:100vh;
    justify-content: center;
    align-items:center;
    width:100%;
    border: 2px solid white;
    background-color:#111827;
    gap:10px;

  }

  

  .editor-wrapper {
    display: flex;
    flex-direction: column;
    align-items: center;
    width: 90%; /* Adjusted width */
    height: 90vh; /* Adjusted height */
    background-color: #030712; /* Box background color */
    padding: 30px;
    border-radius: 10px; /* Rounded corners */
    border: 1px solid #ccc;
  }



  .menu-bar {
    display: flex;
    justify-content: space-between;
    width: 100%;
    margin-bottom: 10px;
  }

  .menu-button {
    color: black; /* Black text */
    border: none;
    padding: 5px 10px;
    text-align: center;
    text-decoration: none;
    display: inline-block;
    font-size: 14px;
    border-radius: 5px; /* Rounded corners */
    cursor: pointer;
    margin-right: 5px;
  }
  .menu-button:hover{
    transform: translate(10px);
  }

  .menu-select {
    background-color: #fff;
    color: black;
  }

  .run-button:disabled {
    background-color: gray; /* Gray background for disabled state */
    cursor: not-allowed; /* Not allowed cursor for disabled state */
  }

  .file-info {
    margin-bottom: 10px;
    color: white;
    font-weight: bold;
  }

  .file-name {
    color: white; /* Text color for file name */
    font-weight: bold; /* Bold text */
    margin-left: 10px;
  }

  .code-textarea {
    background-color:#fafafa; /* Textarea background color */
    color:#2563eb; /* Text color inside textarea */
    font-weight: bold; /* Bold text */
    font-size: 20px; /* Larger font size */
    width: 100%;
    height: 100%; /* Adjusted height */
    border: 1px solid #ccc;
    padding: 10px;
    border-radius: 5px;
    font-family: monospace;
  }

  .green{
    color:green;
    width:40px;
    height:30px;
  }
  .blue{
    color:blue;
    width:40px;
    height:30px;
  }
  .yellow{
    color:yellow;
    width:40px;
    height:30px;

  }
  .red{
    color:red;
    width:40px;
    height:30px;
  }
  .aqua{
    color:aqua;
    width:40px;
    height:30px;
  }
  .aliceblue{
    color:aliceblue;
    width:40px;
    height:30px;
  }
  .white{
    color:white;
    font-size:16px;
    height:40px;
  }
  .language-select {
    margin-right: 10px;
    color:black;
    border: none;
    color: black;
    padding: 5px;
    border-radius: 4px;
    width:100px;
    height:50px;
    cursor: pointer;
  }
  span{
    color:pink;
  }

  .x{
    height:30px;
  }
  .x:hover{
    transform: translate(10px);
  }

</style>
