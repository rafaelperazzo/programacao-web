<?php

class __Mustache_98e7e99d800197bdc25810e2f5385374 extends Mustache_Template
{
    private $lambdaHelper;

    public function renderInternal(Mustache_Context $context, $indent = '')
    {
        $this->lambdaHelper = new Mustache_LambdaHelper($this->mustache, $context);
        $buffer = '';
        $newContext = array();

        // 'hascontent' section
        $value = $context->find('hascontent');
        $buffer .= $this->section1fe273368cf20b1846f8ae930f62378d($context, $indent, $value);

        return $buffer;
    }

    private function section44b12a98e7cbf9df7b425fbae9e7c431(Mustache_Context $context, $indent, $value)
    {
        $buffer = '';
        if (!is_string($value) && is_callable($value)) {
            $source = 'prevpage,tag';
            $result = call_user_func($value, $source, $this->lambdaHelper);
            if (strpos($result, '{{') === false) {
                $buffer .= $result;
            } else {
                $buffer .= $this->mustache
                    ->loadLambda((string) $result)
                    ->renderInternal($context);
            }
        } elseif (!empty($value)) {
            $values = $this->isIterable($value) ? $value : array($value);
            foreach ($values as $value) {
                $context->push($value);
                
                $buffer .= 'prevpage,tag';
                $context->pop();
            }
        }
    
        return $buffer;
    }

    private function sectionE9205ac33c030d700a8844fe5f970d7d(Mustache_Context $context, $indent, $value)
    {
        $buffer = '';
        if (!is_string($value) && is_callable($value)) {
            $source = '
            <a class="gotopage prevpage" href="{{prevpageurl}}" data-quickload="1">{{#str}}prevpage,tag{{/str}}</a>
        ';
            $result = call_user_func($value, $source, $this->lambdaHelper);
            if (strpos($result, '{{') === false) {
                $buffer .= $result;
            } else {
                $buffer .= $this->mustache
                    ->loadLambda((string) $result)
                    ->renderInternal($context);
            }
        } elseif (!empty($value)) {
            $values = $this->isIterable($value) ? $value : array($value);
            foreach ($values as $value) {
                $context->push($value);
                
                $buffer .= $indent . '            <a class="gotopage prevpage" href="';
                $value = $this->resolveValue($context->find('prevpageurl'), $context);
                $buffer .= call_user_func($this->mustache->getEscape(), $value);
                $buffer .= '" data-quickload="1">';
                // 'str' section
                $value = $context->find('str');
                $buffer .= $this->section44b12a98e7cbf9df7b425fbae9e7c431($context, $indent, $value);
                $buffer .= '</a>
';
                $context->pop();
            }
        }
    
        return $buffer;
    }

    private function section7c126982b10933ab1835e4b0d29e27dd(Mustache_Context $context, $indent, $value)
    {
        $buffer = '';
        if (!is_string($value) && is_callable($value)) {
            $source = 'nextpage,tag';
            $result = call_user_func($value, $source, $this->lambdaHelper);
            if (strpos($result, '{{') === false) {
                $buffer .= $result;
            } else {
                $buffer .= $this->mustache
                    ->loadLambda((string) $result)
                    ->renderInternal($context);
            }
        } elseif (!empty($value)) {
            $values = $this->isIterable($value) ? $value : array($value);
            foreach ($values as $value) {
                $context->push($value);
                
                $buffer .= 'nextpage,tag';
                $context->pop();
            }
        }
    
        return $buffer;
    }

    private function section129b4e7680bdaa6af345a757f729f72d(Mustache_Context $context, $indent, $value)
    {
        $buffer = '';
        if (!is_string($value) && is_callable($value)) {
            $source = '
            <a class="gotopage nextpage" href="{{nextpageurl}}" data-quickload="1">{{#str}}nextpage,tag{{/str}}</a>
        ';
            $result = call_user_func($value, $source, $this->lambdaHelper);
            if (strpos($result, '{{') === false) {
                $buffer .= $result;
            } else {
                $buffer .= $this->mustache
                    ->loadLambda((string) $result)
                    ->renderInternal($context);
            }
        } elseif (!empty($value)) {
            $values = $this->isIterable($value) ? $value : array($value);
            foreach ($values as $value) {
                $context->push($value);
                
                $buffer .= $indent . '            <a class="gotopage nextpage" href="';
                $value = $this->resolveValue($context->find('nextpageurl'), $context);
                $buffer .= call_user_func($this->mustache->getEscape(), $value);
                $buffer .= '" data-quickload="1">';
                // 'str' section
                $value = $context->find('str');
                $buffer .= $this->section7c126982b10933ab1835e4b0d29e27dd($context, $indent, $value);
                $buffer .= '</a>
';
                $context->pop();
            }
        }
    
        return $buffer;
    }

    private function section02b4a370062486954ccdbf3b88624352(Mustache_Context $context, $indent, $value)
    {
        $buffer = '';
        if (!is_string($value) && is_callable($value)) {
            $source = '
            <a class="exclusivemode" href="{{exclusiveurl}}">{{exclusivetext}}</a>
        ';
            $result = call_user_func($value, $source, $this->lambdaHelper);
            if (strpos($result, '{{') === false) {
                $buffer .= $result;
            } else {
                $buffer .= $this->mustache
                    ->loadLambda((string) $result)
                    ->renderInternal($context);
            }
        } elseif (!empty($value)) {
            $values = $this->isIterable($value) ? $value : array($value);
            foreach ($values as $value) {
                $context->push($value);
                
                $buffer .= $indent . '            <a class="exclusivemode" href="';
                $value = $this->resolveValue($context->find('exclusiveurl'), $context);
                $buffer .= call_user_func($this->mustache->getEscape(), $value);
                $buffer .= '">';
                $value = $this->resolveValue($context->find('exclusivetext'), $context);
                $buffer .= call_user_func($this->mustache->getEscape(), $value);
                $buffer .= '</a>
';
                $context->pop();
            }
        }
    
        return $buffer;
    }

    private function section1fe273368cf20b1846f8ae930f62378d(Mustache_Context $context, $indent, $value)
    {
        $buffer = '';
        if (!is_string($value) && is_callable($value)) {
            $source = '
<div class="box generalbox tagarea" id="tagarea-{{component}}-{{itemtype}}" data-ta="{{ta}}">
    <a name="{{anchor}}"></a>
    <h3>{{{title}}}</h3>
    <div class="taggeditems">
        {{{content}}}
    </div>
    <div class="controls controls-bottom">
        {{#prevpageurl}}
            <a class="gotopage prevpage" href="{{prevpageurl}}" data-quickload="1">{{#str}}prevpage,tag{{/str}}</a>
        {{/prevpageurl}}
        {{#nextpageurl}}
            <a class="gotopage nextpage" href="{{nextpageurl}}" data-quickload="1">{{#str}}nextpage,tag{{/str}}</a>
        {{/nextpageurl}}
        {{#exclusiveurl}}
            <a class="exclusivemode" href="{{exclusiveurl}}">{{exclusivetext}}</a>
        {{/exclusiveurl}}
    </div>
</div>
';
            $result = call_user_func($value, $source, $this->lambdaHelper);
            if (strpos($result, '{{') === false) {
                $buffer .= $result;
            } else {
                $buffer .= $this->mustache
                    ->loadLambda((string) $result)
                    ->renderInternal($context);
            }
        } elseif (!empty($value)) {
            $values = $this->isIterable($value) ? $value : array($value);
            foreach ($values as $value) {
                $context->push($value);
                
                $buffer .= $indent . '<div class="box generalbox tagarea" id="tagarea-';
                $value = $this->resolveValue($context->find('component'), $context);
                $buffer .= call_user_func($this->mustache->getEscape(), $value);
                $buffer .= '-';
                $value = $this->resolveValue($context->find('itemtype'), $context);
                $buffer .= call_user_func($this->mustache->getEscape(), $value);
                $buffer .= '" data-ta="';
                $value = $this->resolveValue($context->find('ta'), $context);
                $buffer .= call_user_func($this->mustache->getEscape(), $value);
                $buffer .= '">
';
                $buffer .= $indent . '    <a name="';
                $value = $this->resolveValue($context->find('anchor'), $context);
                $buffer .= call_user_func($this->mustache->getEscape(), $value);
                $buffer .= '"></a>
';
                $buffer .= $indent . '    <h3>';
                $value = $this->resolveValue($context->find('title'), $context);
                $buffer .= $value;
                $buffer .= '</h3>
';
                $buffer .= $indent . '    <div class="taggeditems">
';
                $buffer .= $indent . '        ';
                $value = $this->resolveValue($context->find('content'), $context);
                $buffer .= $value;
                $buffer .= '
';
                $buffer .= $indent . '    </div>
';
                $buffer .= $indent . '    <div class="controls controls-bottom">
';
                // 'prevpageurl' section
                $value = $context->find('prevpageurl');
                $buffer .= $this->sectionE9205ac33c030d700a8844fe5f970d7d($context, $indent, $value);
                // 'nextpageurl' section
                $value = $context->find('nextpageurl');
                $buffer .= $this->section129b4e7680bdaa6af345a757f729f72d($context, $indent, $value);
                // 'exclusiveurl' section
                $value = $context->find('exclusiveurl');
                $buffer .= $this->section02b4a370062486954ccdbf3b88624352($context, $indent, $value);
                $buffer .= $indent . '    </div>
';
                $buffer .= $indent . '</div>
';
                $context->pop();
            }
        }
    
        return $buffer;
    }

}
