<template>
  <div>
    <h3 class='center'>Explanation of Word Count</h3>
		<p>
			Changing the word count value will change the amount of words that appear. When 
			the algorithm goes through words that do not appear as many times as the word 
			count value will not change. This feature will allow users to zoom in on text files 
			that are really long. The test file that was used here was short and thus the 
			word count value is defaulted to 3. 
		</p>
  </div>
</template>

<script>
export default {
  name: "WordCountExplanation",
};
</script>

<style scoped>
</style>