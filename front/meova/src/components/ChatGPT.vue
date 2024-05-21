<template>
    <div>
      <h1>Chat GPT</h1>
      <div>
        <div v-for="message in messages" :key="message.id">
          <p v-if="message.type === 'user'">{{ message.text }}</p>
          <p v-else-if="message.type === 'bot'">{{ message.text }}</p>
        </div>
      </div>
      <input v-model="userMessage" @keyup.enter="sendMessage" placeholder="Type your message...">
    </div>
  </template>
  
  <script setup>
  import { ref } from 'vue'
  import OpenAI from 'openai'
  
  // OpenAI API 설정
  const apiKey = 'sk-proj-MkFuOqkKJ88Q9az12B3HT3BlbkFJFbIdzIWOjXYCbmvNl0R0'
  const openai = new OpenAI({ apiKey, dangerouslyAllowBrowser: true });
  
  const userMessage = ref('')
  const messages = ref([])
  
  // 사용자 메시지 전송
  const sendMessage = async () => {
    const text = userMessage.value
    messages.value.push({ id: messages.value.length, type: 'user', text })
  
    // OpenAI에 메시지 전송
    try {
      const response = await openai.createCompletion({
        model: 'gpt-3.5-turbo', // GPT-3.5 모델
        prompt: text,
        maxTokens: 150 // 수정된 옵션
      })
      const botResponse = response.data.choices[0].text.trim()
      messages.value.push({ id: messages.value.length, type: 'bot', text: botResponse })
    } catch (error) {
      console.error('Error fetching response from OpenAI:', error)
    }
  
    userMessage.value = ''
  }
  </script>
  
  <style scoped>
  /* 추가 스타일링 */
  </style>
  