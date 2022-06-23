<p>给定两个数组，<code>arr1</code> 和&nbsp;<code>arr2</code>，</p>

<ul>
	<li><code>arr2</code>&nbsp;中的元素各不相同</li>
	<li><code>arr2</code> 中的每个元素都出现在&nbsp;<code>arr1</code>&nbsp;中</li>
</ul>

<p>对 <code>arr1</code>&nbsp;中的元素进行排序，使 <code>arr1</code> 中项的相对顺序和&nbsp;<code>arr2</code>&nbsp;中的相对顺序相同。未在&nbsp;<code>arr2</code>&nbsp;中出现过的元素需要按照升序放在&nbsp;<code>arr1</code>&nbsp;的末尾。</p>

<p>&nbsp;</p>

<p><strong>示例：</strong></p>

<pre>
<strong>输入：</strong>arr1 = [2,3,1,3,2,4,6,7,9,2,19], arr2 = [2,1,4,3,9,6]
<strong>输出：</strong>[2,2,2,1,4,3,3,9,6,7,19]
</pre>

<p>&nbsp;</p>

<p><strong>提示：</strong></p>

<ul>
	<li><code>1 &lt;= arr1.length, arr2.length &lt;= 1000</code></li>
	<li><code>0 &lt;= arr1[i], arr2[i] &lt;= 1000</code></li>
	<li><code>arr2</code>&nbsp;中的元素&nbsp;<code>arr2[i]</code>&nbsp;各不相同</li>
	<li><code>arr2</code> 中的每个元素&nbsp;<code>arr2[i]</code>&nbsp;都出现在&nbsp;<code>arr1</code>&nbsp;中</li>
</ul>

<p>&nbsp;</p>

<p><meta charset="UTF-8" />注意：本题与主站 1122&nbsp;题相同：<a href="https://leetcode-cn.com/problems/relative-sort-array/">https://leetcode-cn.com/problems/relative-sort-array/</a>&nbsp;</p>
<div><div>Related Topics</div><div><li>数组</li><li>哈希表</li><li>计数排序</li><li>排序</li></div></div><br><div><li>👍 24</li><li>👎 0</li></div>