# Some breakpoints may indicate an out-of-memory error, heap corruption, or no error at all:
dtxErrorTranslations = {
  "OOM": (
    "The process triggered a breakpoint to indicate it was unable to allocate enough memory",
    None,
    [
      [     # Chrome
        "chrome.dll!base::`anonymous namespace'::OnNoMemory",
      ], [
        "chrome_child.dll!base::`anonymous namespace'::OnNoMemory",
      ], [
        "chrome.dll!base::debug::BreakDebugger",
        "chrome.dll!logging::LogMessage::~LogMessage",
        "chrome.dll!base::`anonymous namespace'::OnNoMemory",
      ], [
        "chrome_child.dll!base::debug::BreakDebugger",
        "chrome_child.dll!logging::LogMessage::~LogMessage",
        "chrome_child.dll!base::`anonymous namespace'::OnNoMemory",
      ], [
        "chrome_child.dll!base::debug::BreakDebugger",
        "chrome_child.dll!content::`anonymous namespace'::CrashOnMapFailure",
      ], [
        "chrome_child.dll!blink::reportFatalErrorInMainThread",
        "chrome_child.dll!v8::Utils::ReportApiFailure",
        "chrome_child.dll!v8::Utils::ApiCheck",
        "chrome_child.dll!v8::internal::V8::FatalProcessOutOfMemory",
      ], [  # Edge
        "KERNELBASE.dll!RaiseException",
        "EDGEHTML.dll!Abandonment::InduceAbandonment",
        "EDGEHTML.dll!Abandonment::OutOfMemory",
      ], [  # Firefox
        "mozglue.dll!mozalloc_abort",
        "mozglue.dll!mozalloc_handle_oom",
      ], [  # Firefox
        "mozglue.dll!moz_abort",
        "mozglue.dll!pages_commit",
      ], [
        "xul.dll!js::CrashAtUnhandlableOOM",
      ], [
        "xul.dll!NS_ABORT_OOM",
      ], [  # MSIE
        "KERNELBASE.dll!DebugBreak",
        "jscript9.dll!ReportFatalException",
        "jscript9.dll!JavascriptDispatch_OOM_fatal_error",
      ],
    ],
  ),
  "HeapCorrupt": (
    "A corrupted heap block was detected",
    "This is probably an exploitable security issue",
    [
      [
        "verifier.dll!VerifierStopMessage",
        "verifier.dll!AVrfpDphReportCorruptedBlock",
      ],
    ],
  ),
  "Assert": (
    "An assertion failed",
    None,
    [
      [ # Edge
        "KERNELBASE.dll!RaiseException",
        "EDGEHTML.dll!Abandonment::InduceAbandonment",
        "EDGEHTML.dll!Abandonment::AssertionFailed",
      ], [
        "KERNELBASE.dll!RaiseException",
        "EDGEHTML.dll!Abandonment::InduceAbandonment",
        "EDGEHTML.dll!Abandonment::CheckHRESULT",
      ], [
        "KERNELBASE.dll!RaiseException",
        "EDGEHTML.dll!Abandonment::InduceAbandonment",
        "EDGEHTML.dll!Abandonment::FastDOMInvariantViolation",
      ],
    ],
  ),
  # When a 32-bit application is running on a 64-bit OS, any new processes will generate a STATUS_BREAKPOINT and
  # a status STATUS_WX86_BREAKPOINT exception. The former is recognized as the initial process breakpoint, and the
  # new process is registered. The later is not, but it can be recognized by its stack and should be ignored:
  None: (
    None,
    None,
    [
      [
        "ntdll.dll!LdrpDoDebuggerBreak",
        "ntdll.dll!LdrpInitializeProcess",
      ],
    ],
  ),
};

# Hide some functions at the top of the stack that are merely helper functions and not relevant to the error:
asHiddenTopFrames = [
  "kernel32.dll!DebugBreak",
  "KERNELBASE.dll!DebugBreak",
  "ntdll.dll!DbgBreakPoint",
  "EDGEHTML.dll!Abandonment::AssertionFailed",
  "EDGEHTML.dll!Abandonment::Fail",
  "EDGEHTML.dll!Abandonment::InduceAbandonment",
  "chrome.dll!base::debug::BreakDebugger",
  "chrome_child.dll!base::debug::BreakDebugger",
  # Special "HeapCorrupt" cases:
  "chrome_child.dll!_aligned_free",
  "chrome_child.dll!`anonymous namespace'::win_heap_free",
  "kernel32.dll!HeapFree",
  "ntdll.dll!RtlDebugFreeHeap",
  "ntdll.dll!RtlFreeHeap",
  "ntdll.dll!RtlpFreeHeap",
  "verifier.dll!AVrfDebugPageHeapFree",
  "verifier.dll!AVrfpDphCheckPageHeapBlock",
  "verifier.dll!AVrfpDphFindBusyMemory",
  "verifier.dll!AVrfpDphFindBusyMemoryAndRemoveFromBusyList",
  # Special "OOM" cases
  "chrome.dll!`anonymous namespace'::call_new_handler",
  "chrome.dll!`anonymous namespace'::generic_cpp_alloc",
  "chrome.dll!malloc",
  "chrome.dll!operator new",
  "chrome.dll!operator new[]",
  "chrome.dll!realloc",
  "chrome.dll!std::_Allocate",
  "chrome.dll!std::_Allocate<...>",
  "chrome.dll!std::allocator<...>::allocate",
  "chrome.dll!std::allocator<...>::allocate",
  "chrome.dll!std::basic_string<...>::append",
  "chrome.dll!std::basic_string<...>::assign",
  "chrome.dll!std::basic_string<...>::_Copy",
  "chrome.dll!std::basic_string<...>::{ctor}",
  "chrome.dll!std::basic_string<...>::_Grow",
  "chrome.dll!std::deque<...>::emplace_back<>",
  "chrome.dll!std::deque<...>::_Growmap",
  "chrome.dll!std::deque<...>::insert",
  "chrome.dll!std::deque<...>::push_back",
  "chrome.dll!std::deque<...>::resize",
  "chrome.dll!std::_Hash<...>::_Check_size",
  "chrome.dll!std::_Hash<...>::emplace",
  "chrome.dll!std::_Hash<...>::_Init",
  "chrome.dll!std::_Hash<...>::_Insert<...>",
  "chrome.dll!std::unordered_map<...>::operator[]",
  "chrome.dll!std::vector<...>::assign",
  "chrome.dll!std::vector<...>::_Buy",
  "chrome.dll!std::vector<...>::insert",
  "chrome.dll!std::vector<...>::_Insert_n",
  "chrome.dll!std::vector<...>::_Reallocate",
  "chrome.dll!std::_Wrap_alloc<...>::allocate",
  "chrome_child.dll!blink::DOMArrayBuffer::create",
  "chrome_child.dll!blink::DOMTypedArray<...>::create",
  "chrome_child.dll!blink::PurgeableVector::append",
  "chrome_child.dll!blink::PurgeableVector::reservePurgeableCapacity",
  "chrome_child.dll!blink::RawResource::appendData",
  "chrome_child.dll!blink::Resource::appendData",
  "chrome_child.dll!blink::SharedBuffer::append",
  "chrome_child.dll!blink::SharedBuffer::SharedBuffer",
  "chrome_child.dll!blink::ContiguousContainer<...>::allocateAndConstruct",
  "chrome_child.dll!blink::ContiguousContainer<...>::allocateAndConstruct<...>",
  "chrome_child.dll!blink::ContiguousContainer<...>::appendByMoving",
  "chrome_child.dll!blink::ContiguousContainer<...>::{ctor}",
  "chrome_child.dll!blink::ContiguousContainerBase::allocate",
  "chrome_child.dll!blink::ContiguousContainerBase::allocateNewBufferForNextAllocation",
  "chrome_child.dll!blink::ContiguousContainerBase::Buffer::Buffer",
  "chrome_child.dll!blink::ContiguousContainerBase::ContiguousContainerBase",
  "chrome_child.dll!content::`anonymous namespace'::CrashOnMapFailure",
  "chrome_child.dll!v8::internal::Factory::NewRawOneByteString",
  "chrome_child.dll!v8::internal::Factory::NewRawTwoByteString",
  "chrome_child.dll!v8::internal::Factory::NewUninitializedFixedArray",
  "chrome_child.dll!v8::internal::Heap::AllocateRawFixedArray",
  "chrome_child.dll!v8::internal::Heap::AllocateUninitializedFixedArray",
  "chrome_child.dll!v8::internal::Heap::FatalProcessOutOfMemory",
  "chrome_child.dll!WTF::ArrayBuffer::create",
  "chrome_child.dll!WTF::DefaultAllocator::allocateBacking",
  "chrome_child.dll!WTF::DefaultAllocator::allocateExpandedVectorBacking",
  "chrome_child.dll!WTF::DefaultAllocator::allocateVectorBacking",
  "chrome_child.dll!WTF::DefaultAllocator::allocateZeroedHashTableBacking<...>",
  "chrome_child.dll!WTF::fastMalloc",
  "chrome_child.dll!WTF::HashMap<...>::inlineAdd",
  "chrome_child.dll!WTF::HashTable<...>::add<...>",
  "chrome_child.dll!WTF::HashTable<...>::allocateTable",
  "chrome_child.dll!WTF::HashTable<...>::expand",
  "chrome_child.dll!WTF::HashTable<...>::rehash",
  "chrome_child.dll!WTF::partitionAlloc",
  "chrome_child.dll!WTF::partitionAllocGeneric",
  "chrome_child.dll!WTF::partitionAllocGenericFlags",
  "chrome_child.dll!WTF::partitionAllocSlowPath",
  "chrome_child.dll!WTF::partitionBucketAlloc",
  "chrome_child.dll!WTF::partitionOutOfMemory",
  "chrome_child.dll!WTF::partitionReallocGeneric",
  "chrome_child.dll!WTF::Partitions::bufferMalloc",
  "chrome_child.dll!WTF::Partitions::bufferRealloc",
  "chrome_child.dll!WTF::RefCounted<...>::operator new",
  "chrome_child.dll!WTF::String::utf8",
  "chrome_child.dll!WTF::StringBuilder::append",
  "chrome_child.dll!WTF::StringBuilder::appendUninitialized",
  "chrome_child.dll!WTF::StringBuilder::appendUninitializedSlow<...>",
  "chrome_child.dll!WTF::StringBuilder::reallocateBuffer<...>",
  "chrome_child.dll!WTF::StringImpl::operator new",
  "chrome_child.dll!WTF::StringImpl::reallocate",
  "chrome_child.dll!WTF::TypedArrayBase<...>::create<...>",
  "chrome_child.dll!WTF::Uint8ClampedArray::create",
  "chrome_child.dll!WTF::Vector<...>::append",
  "chrome_child.dll!WTF::Vector<...>::appendSlowCase<...>",
  "chrome_child.dll!WTF::Vector<...>::expandCapacity",
  "chrome_child.dll!WTF::Vector<...>::extendCapacity",
  "chrome_child.dll!WTF::Vector<...>::reserveCapacity",
  "chrome_child.dll!WTF::Vector<...>::reserveInitialCapacity ",
  "chrome_child.dll!WTF::Vector<...>::resize",
  "chrome_child.dll!WTF::Vector<...>::Vector<...>",
  "chrome_child.dll!WTF::VectorBuffer<...>::VectorBuffer<...>",
  "chrome_child.dll!WTF::VectorBuffer<...>::allocateExpandedBuffer",
  "chrome_child.dll!WTF::VectorBufferBase<...>::allocateBuffer",
  "chrome_child.dll!WTF::VectorBufferBase<...>::allocateExpandedBuffer",
  "jscript9.dll!JavascriptDispatch_OOM_fatal_error",
  "jscript9.dll!Js::Exception::RaiseIfScriptActive",
  "mozglue.dll!arena_malloc_large",
  "mozglue.dll!arena_run_split",
  "mozglue.dll!je_malloc",
  "mozglue.dll!moz_xcalloc",
  "mozglue.dll!moz_xmalloc",
  "mozglue.dll!moz_xrealloc",
  "mozglue.dll!mozalloc_abort",
  "mozglue.dll!mozalloc_handle_oom",
  "mozglue.dll!pages_commit",
  "xul.dll!js::CrashAtUnhandlableOOM",
  "xul.dll!js::MallocProvider<...>",
  "xul.dll!mozilla::CircularByteBuffer::SetCapacity",
  "xul.dll!NS_ABORT_OOM",
  "xul.dll!nsAString_internal::nsAString_internal",
  "xul.dll!nsACString_internal::AppendFunc",
  "xul.dll!nsBaseHashtable<...>::Put",
  "xul.dll!nsBaseHashtable::Put",
  "xul.dll!nsGlobalWindow::ClearDocumentDependentSlots",
  "xul.dll!nsPresArena::Allocate",
  "xul.dll!nsTArray_base<...>::EnsureCapacity",
  "xul.dll!nsTArray_Impl<...>::AppendElements",
  "xul.dll!nsTArray_Impl<...>::AppendElement<...>",
  "xul.dll!StatsCompartmentCallback",
  "xul.dll!std::_Allocate<char>",
  "xul.dll!std::basic_string<...>::_Copy",
  "xul.dll!std::basic_string<...>::assign",
  "xul.dll!std::vector<...>::_Reallocate",
  "xul.dll!std::vector<...>::_Reserve",
];
def cErrorReport_foSpecialErrorReport_STATUS_BREAKPOINT(oErrorReport, oCdbWrapper):
  oErrorReport = oErrorReport.foTranslateError(dtxErrorTranslations);
  if oErrorReport:
    oErrorReport.oStack.fHideTopFrames(asHiddenTopFrames);
  return oErrorReport;
