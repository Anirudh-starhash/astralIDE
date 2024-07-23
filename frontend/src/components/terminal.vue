<template>
    <div class="right">
        <h1>Terminal</h1>
        <h2>Localuser/</h2>
        <div class="terminal-input">
          <select id="terminalType" v-model="commandtype" @onchange="updateTerminal">
            <option value="bash$">Bash</option>
            <option value="cmd_C:\\">Cmd</option>
            <option value="pwshC://">Powershell</option>
            <option value="ubun$">Ubuntu</option>
          </select>
         
          
        </div>

        <div class="terminal-input">
          <h3>{{commandtype.substring(4,commandtype.length)}}</h3>
          <input type="text" id="commandInput" placeholder="Type your command here..." spellcheck="false">
        </div>
        
       
    </div>
</template>

<script>
  export default{
    name:'terminal',
    data(){
        return{
            commandtype:'bash$'
        }
    },
  }
</script>

<style scoped>
h1 {
    text-align: center;
    color:#4ade80;
  }
  h2{
    color:#2563eb;
  }
  h3{
    color:gainsboro;
  }
  .right {
    display: flex;
    flex-direction: column;
    border: 2px solid white; /* Adjust the border color as needed */
    padding:20px;
    width: 40%;; /* Adjust the width as needed */
    min-height:100vh;
    background-color: #020617
  }

  .terminal-input {
    display: flex;
    align-items: center;
    color:black;
    font-weight: bold;
    gap:10px;
  }
  
  #terminalType {
    margin-right: 10px;
    padding: 5px;
  }
  
  #commandInput {
    font-weight: bold;
    padding: 5px;
    border: 1px solid #ccc;
    color:white;
    border-radius: 3px;
    background-color: black;

  }
</style>