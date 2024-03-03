<template>

</template>

<script setup>
import { onMounted } from 'vue';
import { useRouter } from 'vue-router';

const router = useRouter();

onMounted(() => {
  // PDFのURLは、実際のアプリケーションの要件に合わせて変更してください。
  const pdfUrl = 'ここにPDFのURLを設定';
  window.open(pdfUrl, '_blank');
  // PDFを開いた後、ユーザーをリダイレクトしたい場合は、ここでリダイレクト処理を追加
  // 例: router.push('/home');
});
</script>
